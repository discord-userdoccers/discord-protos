// Map the type ints to their names
const ScalarType = {
    1: "double",
    2: "float",
    3: "int64",
    4: "uint64",
    5: "int32",
    6: "fixed64",
    7: "fixed32",
    8: "bool",
    9: "string",
    12: "bytes",
    13: "uint32",
    15: "sfixed32",
    16: "sfixed64",
    17: "sint32",
    18: "sint64",
};
const RepeatType = {
    NO: 0,
    PACKED: 1,
    UNPACKED: 2,
};

function parseType(field) {
    // We extract the actual field if possible
    if (typeof field === "function") {
        field = field();
        // If it's a real type, we just return it
    } else if (typeof field === "number") {
        return [ScalarType[field], []];
    }

    var type,
        structs = [];

    // The kind gives us clues on how to find the type
    switch (field.kind) {
        case "message":
            type = field.T().typeName;
            if (type.startsWith("discord")) {
                [, type] = parseName(type);
            }
            break;
        case "scalar":
            type = ScalarType[field.T];
            break;
        case "map":
            type = `map<${parseType(field.K)[0]}, ${parseType(field.V)[0]}>`;
            break;
        case "enum":
            [, type] = parseName(field.T()[0]);
            break;
        default:
            throw new Error(`Unknown field type: ${field?.kind || field}`);
    }

    // Now we lazily discover any protos in the fields
    for (let t of [field.T, field.K, field.V]) {
        t = t?.T || t;

        if (typeof t === "function" && (!t().typeName || t().typeName.startsWith("discord_protos"))) {
            t = t();
            if (Array.isArray(t)) {
                structs.push(parseEnum(t));
            } else {
                const extraStruct = parseProto(t);
                structs.push(...(extraStruct.structs || []));
                delete extraStruct.structs;
                structs.push(extraStruct);
            }
        }
    }

    return [type, structs];
}

function parseName(name) {
    const split = name.split(".");
    return [split.slice(0, -1).join("."), split.slice(-1)[0]];
}

function convertCase(str) {
    // This converts standard EnumType case to ENUM_TYPE
    // it must support the special case SlayerSDKReceive to SLAYER_SDK_RECEIVE
    return str
        // HACK: I can't think of another way to fix this
        .replace("DMs", "Dms")
        .replace(/([a-z])([A-Z])/g, "$1_$2")
        .replace(/([A-Z])([A-Z][a-z])/g, "$1_$2")
        .replace(/([a-z])(\d)/g, "$1_$2")
        .replace(/([A-Z]+)(?=[A-Z][a-z])/g, "$1_")
        .toUpperCase();
}

function camelToSnake(str) {
    return str.replace(/(([a-z])(?=[A-Z][a-zA-Z])|([A-Z])(?=[A-Z][a-z]))/g,'$1_').toLowerCase()
}

function flattenField(field) {
    const [type, structs] = parseType(field);
    return [
        {
            number: field.no,
            name: field.name,
            kind: field.kind,
            type: type,
            oneof: field.oneof,
            optional: field.opt,
            repeated: Boolean(field.repeat),
            unpacked: field.repeat === RepeatType.UNPACKED,
        },
        structs,
    ];
}

function parseEnum(enun) {
    const [name, data] = enun;

    // Protobuf enum values conventionally have a prefix of NAME_ and we must add that back
    const [, formattedName] = parseName(name);
    const prefix = convertCase(formattedName) + "_";

    return {
        name: formattedName,
        kind: "enum",
        values: Object.entries(data)
            .filter(([k, _]) => isNaN(Number(k)))
            .map(([k, v]) => ({
                // Discord shitcode sometimes fails to strip the prefix on the special case
                // so we check if it already has it
                name: k.startsWith(prefix) ? k : prefix + k,
                value: v,
            })),
    };
}

function parseProto(proto) {
    const fields = [];
    const structs = [];
    proto.fields.forEach(function (field) {
        const [f, s] = flattenField(field);
        fields.push(f);
        structs.push(...s);
    });

    const seen = new Set();
    const [package, name] = parseName(proto.typeName);
    return {
        package,
        name,
        kind: "message",
        fields: fields,
        structs: structs.filter((v) => (seen.has(v.name) ? false : seen.add(v.name))),
    };
}

function extractProtos() {
    const results = {};

    // Populated by preload.js
    for (const proto of window.protoObjects) {
        if (!proto?.typeName?.startsWith?.("discord_protos")) continue;
        const [, name] = parseName(proto.typeName);
        console.log(`Parsing ${name}...`);
        results[name] = parseProto(proto);
    }

    // Remove every proto that is mentioned in another proto
    for (const proto of Object.values(results)) {
        for (const struct of proto.structs) {
            delete results[struct.name];
        }
    }

    return results;
}

function createProtoField(field) {
    if (!field.repeated && field.unpacked)
        throw new Error(`Field ${field.name} is not repeated but has unpacked set`);
    return `${field.optional ? "optional " : field.repeated ? "repeated " : ""}${field.type} ${field.name} = ${field.number}${field.unpacked ? " [packed = false]" : ""};`;
}

function createProtoFile(proto) {
    const lines = [`syntax = "proto3";\n`, `package ${proto.package};\n`, `message ${proto.name} {`];

    proto.structs.forEach((struct) => {
        lines.push(`  ${struct.kind} ${struct.name} {`);

        switch (struct.kind) {
            case "enum":
                struct.values.forEach((value) => {
                    lines.push(`    ${value.name.toUpperCase()} = ${value.value};`);
                });
                break;
            case "message":
                // Group fields by oneof if applicable
                const oneofGroups = new Map();
                const normalFields = [];
                
                struct.fields.forEach((field) => {
                    if (field.oneof) {
                        if (!oneofGroups.has(field.oneof)) {
                            oneofGroups.set(field.oneof, []);
                        }
                        oneofGroups.get(field.oneof).push(field);
                    } else {
                        normalFields.push(field);
                    }
                });

                oneofGroups.forEach((fields, oneofName) => {
                    lines.push(`    oneof ${camelToSnake(oneofName)} {`);
                    fields.forEach((field) => {
                        lines.push(`      ${createProtoField(field)}`);
                    });
                    lines.push(`    }`);
                });

                normalFields.forEach((field) => {
                    lines.push(`    ${createProtoField(field)}`);
                });
                break;
            default:
                throw new Error(`Unknown struct kind: ${struct.kind}`);
        }

        lines.push(`  }\n`);
    });

    const oneofGroups = new Map();

    proto.fields.forEach((field) => {
        if (field.oneof) {
            if (!oneofGroups.has(field.oneof)) {
                oneofGroups.set(field.oneof, []);
            }
            oneofGroups.get(field.oneof).push(createProtoField(field));
        } else {
            lines.push(`  ${createProtoField(field)}`);
        }
    });

    oneofGroups.forEach((fields, oneofName) => {
        lines.push(`  oneof ${camelToSnake(oneofName)} {`);
        fields.forEach(field => lines.push(`    ${field}`));
        lines.push(`  }\n`);
    });

    // Check if we're using the funny Google well-knowns and insert an import statement (I love Discord)
    if (lines.some((line) => line.includes("google.protobuf"))) {
        lines.splice(1, 0, `import "google/protobuf/wrappers.proto";\nimport "google/protobuf/timestamp.proto";\n`);
    }

    lines.push("}\n");
    return lines.join("\n");
}

const protos = extractProtos();
for (const [key, proto] of Object.entries(protos)) {
    const data = createProtoFile(proto);
    protos[key].data = data;
    if (window.DiscordNative?.fileManager) {
        window.DiscordNative.fileManager.saveWithDialog(data, `${proto.name}.proto`);
    } else {
        console.log(data);
    }
}
