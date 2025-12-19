import { MessageType } from "@protobuf-ts/runtime";

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

export * from "./discord_protos/users/v1/User";
export * from "./discord_protos/users/v1/MediumUser";
export * from "./discord_protos/users/v1/UserData";
export * from "./discord_protos/users/v1/GuildShardingConfig";
export * from "./discord_protos/discord_experimentation/v1/Experiment";
export * from "./discord_protos/discord_users/v1/PreloadedUserSettings";
export * from "./discord_protos/discord_users/v1/FrecencyUserSettings";
export * from "./discord_protos/discord_kkv_store_value_models/v1/ApplicationUserRoleConnection";
export * from "./discord_protos/discord_kkv_store_value_models/v1/AcknowledgedApplicationDisclosures";
export * from "./discord_protos/premium_marketing/v1/PremiumMarketingComponentProperties";
