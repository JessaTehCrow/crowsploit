# crowsploit
A hack tool for the game greyhack aimed to be the gmod of tools.

## Building crowsploit

**Make sure you have the vscode greybel addon installed**

### Prerequisites

- Make sure greybel has `allow import` **TURNED OFF** in the settings
- Set `Greybel › Transpiler › Installer` to true
- Do **NOT** use obfuscation, this will destroy crowsploit


### Building interface

All you need to build the crowsploit interface, is build the `interface/crowsploit` file into the game.

### Building tools

All tools must have toolkernel as an import, and `tool.init()` at the bottom.

Additional tools can be imported into the same tool by just using `import_code(tool_path)` at the end of the file (Make sure to do this AFTER the .init)

### Building Devtools

Turn ON the allow import in greybel settings, before building the devtools

***MAKE SURE TO TURN IT RIGHT BACK OFF AFTERWARDS***