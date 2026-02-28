# Discord Protocol Buffers
Reverse-engineering Discord's protobufs.

This repository provides protocol buffer files for all protobufs found in Discord's client source, automatically generated and automatically updated. The protobufs are provided as .proto files in the `out/` directory.

These protobufs are used by Discord clients for transmitting data like user settings and premium marketing.

## Usage

### Installation

Note: These packages are automatically updated when changes are detected in the protobufs. As Discord often updates their protobufs, pinning to a specific version may be advisable.

```
# with npm
npm install discord-protos

# with yarn
yarn add discord-protos

# with pnpm
pnpm add discord-protos

# with pip
pip install discord-protos
```

### Example
JavaScript:
```js
const { PreloadedUserSettings } = require('discord-protos');

const encoded = PreloadedUserSettings.toBase64({
    status: {
        status: {
            value: "online",
        },
        customStatus: {
            text: "Hello World",
            emojiId: 0n,
            emojiName: "",
            expiresAtMs: 0n,
            createdAtMs: 0n,
        },
    },
});

const decoded = PreloadedUserSettings.fromBase64(encoded);

console.log(encoded, decoded);
```

Python:
```py
import base64

from google.protobuf.json_format import ParseDict
from discord_protos import PreloadedUserSettings

settings = PreloadedUserSettings()
payload = ParseDict({
    'status': {
        'status': 'online',
        'custom_status': {
            'text': 'Hello World',
        },
    },
}, settings).SerializeToString()

encoded = base64.b64encode(payload).decode('ascii')
decoded = PreloadedUserSettings.FromString(base64.b64decode(encoded))

print(encoded, decoded, sep='\n')
```

The following table shows which protobuf user settings correspond to which .proto file (the Python package also provides a `UserSettingsType` enum for convenience).

| Type | Value                             | File                        | Use                                                |
| ---- | --------------------------------- | --------------------------- | -------------------------------------------------- |
| 1    | `PRELOADED_USER_SETTINGS`         | PreloadedUserSettings.proto | General Discord user settings.                     |
| 2    | `FRECENCY_AND_FAVORITES_SETTINGS` | FrecencyUserSettings.proto  | Frecency and favorites storage for various things. |
| 3    | `TEST_SETTINGS`                   | -                           | Unknown.                                           |

See [Userdoccers](https://docs.discord.food/resources/user-settings-proto) for more information.

### Development
Running `pnpm load` will extract and save the latest protobufs to the `discord_protos/` directory.
