import puppeteer from "puppeteer";
import { writeFileSync, readFileSync, mkdirSync, existsSync, readdirSync, rmSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";

// For the JS template, all we need to do is update the exports at the bottom
const JS_TEMPLATE = `import { MessageType } from "@protobuf-ts/runtime";

/**
 * Supports both node and web environments, replacement of previous Buffer.from() being node-only.
 * This is specific to this package's usage, and not a replacement of Buffer.from() altogether
 */
const compatBuffer = {
    from: function (input: string | Uint8Array, encoding?: string) {
        if (typeof input === "string" && encoding === "base64") {
            const encodedBytes = atob(input);
            const bytes = new Uint8Array(encodedBytes.length);
            for (let i = 0; i < encodedBytes.length; i++) {
                bytes[i] = encodedBytes.charCodeAt(i);
            }
            return bytes;
        } else if (!encoding && input instanceof Uint8Array) {
            return input;
        }
        throw new Error("Invalid input type.");
    },
    toBase64String: function (buffer: Uint8Array) {
        let encodedBytes = "";
        for (let i = 0; i < buffer.length; i++) {
            encodedBytes += String.fromCharCode(buffer[i]);
        }
        return btoa(encodedBytes);
    },
};

function toBase64(this: MessageType<any>, data) {
    return compatBuffer.toBase64String(compatBuffer.from(this.toBinary(data)));
}

function fromBase64(this: MessageType<any>, base64: string) {
    return this.fromBinary(compatBuffer.from(base64, "base64"));
}

declare module "@protobuf-ts/runtime" {
    interface MessageType<T> {
        toBase64(data: T): string;
        fromBase64(base64: string): T;
    }
}

MessageType.prototype.fromBase64 = fromBase64;
MessageType.prototype.toBase64 = toBase64;

{{ protos_exports }}
`;

// For the Python template, we need to update both imports and the __all__ variable, as well as bump the version number
const PY_TEMPLATE = `from __future__ import annotations

from enum import Enum as _Enum
from typing import TYPE_CHECKING

__version__ = '{{ version }}'

if TYPE_CHECKING:
    from google.protobuf.message import Message as _Message

    {{ protos_equals }} = _Message
else:
{{ protos_imports }}

__all__ = (
    '__version__',
    'UserSettingsType',
{{ exports }}
)


class UserSettingsType(_Enum):
    preloaded_user_settings = 1
    frecency_user_settings = 2
    test_settings = 3


UserSettingsImpl = {
    UserSettingsType.preloaded_user_settings: PreloadedUserSettings,
    UserSettingsType.frecency_user_settings: FrecencyUserSettings,
    UserSettingsType.test_settings: None,
}
`;

// This must be run early
const PRELOAD_SCRIPT = readFileSync(join(__dirname, "..", "scripts", "preload.js"), "utf8");
const PARSE_SCRIPT = readFileSync(join(__dirname, "..", "scripts", "parse.js"), "utf8");

async function main() {
    const browser = await puppeteer.launch();

    const page = await browser.newPage();
    page.on("console", (msg) => console.debug(msg.text()));

    // Preload script grabs the objects
    await page.evaluateOnNewDocument(PRELOAD_SCRIPT);
    await page.goto("https://canary.discord.com/app", { waitUntil: "networkidle0" });

    const protos = await page.evaluate(`${PARSE_SCRIPT}; protos`);
    await browser.close();

    // Delete all existing files and folders in the discord_protos directory
    const outputs = [join(__dirname, "..", "discord_protos"), join(__dirname, "..", "src", "discord_protos")];
    for (const output of outputs) {
        if (existsSync(output)) {
            for (const file of readdirSync(output)) {
                rmSync(join(output, file), { recursive: true, force: true });
            }
        }
    }

    // Write the protos to disk
    const filenames = []
    for (const [name, proto] of Object.entries(protos)) {
        const dir = join(__dirname, "..", ...proto.package.split("."));
        const filename = join(dir, `${name}.proto`);
        filenames.push(filename.replace(join(__dirname, ".."), ".").replaceAll("\\", "/"));

        // Ensure the directory exists
        if (!existsSync(dir)) {
            mkdirSync(dir, { recursive: true });
        }
        writeFileSync(filename, proto.data);
    }

    // Check if we have any changes using git
    const changes = execSync("git status --porcelain").toString().trim();
    if (!changes.includes(".proto")) {
        console.log("No changes detected, exiting...");
        return;
    }

    const packageJson = JSON.parse(readFileSync(join(__dirname, "..", "package.json"), "utf8"));

    // Bump the version number
    const version = packageJson.version.split(".").map((x: string) => parseInt(x)).map((x: number, i: number) => i === 2 ? x + 1 : x).join(".");
    packageJson.version = version;

    // This is very cursed
    // For protoc to parse any new protos, we have to edit the script in the package.json to include the filenames
    const js = packageJson.scripts.js.split(" ").filter((x) => !x.endsWith(".proto")).join(" ");
    const py = packageJson.scripts.py.split(" ").filter((x) => !x.endsWith(".proto")).join(" ");
    packageJson.scripts.js = `${js} ${filenames.join(" ")}`;
    packageJson.scripts.py = `${py} ${filenames.join(" ")}`;
    writeFileSync(join(__dirname, "..", "package.json"), JSON.stringify(packageJson, null, 4));

    // Update the JS template
    const jsExports = filenames.map((x) => `export * from "${x.replaceAll("\\", "/").replace(".proto", "")}";`).join("\n");
    writeFileSync(join(__dirname, "..", "src", "index.ts"), JS_TEMPLATE.replace("{{ protos_exports }}", jsExports));

    // Update the Python template
    const pyExports = Object.keys(protos).map((x) => `    '${x}',`).join("\n");
    const pyImports = filenames.map((x) => `    from ${x.replaceAll("\\", "/").replace("./discord_protos", "").replaceAll("/", ".").replace(".proto", "_pb2")} import *`).join("\n");
    const pyEquals = Object.keys(protos).join(" = ");
    writeFileSync(
        join(__dirname, "..", "discord_protos", "__init__.py"),
        PY_TEMPLATE.replace("{{ version }}", version).replace("{{ exports }}", pyExports).replace("{{ protos_imports }}", pyImports).replace("{{ protos_equals }}", pyEquals)
);
}

main();
