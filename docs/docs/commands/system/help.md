# Help

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `system`

```shell
help tool|command? command? --small
```

Shows help for specific tools and or commands

## Arguments

| Name | type | required | info |
|------|------|----------|------|
| tool\|command | string | :octicons-x-16: | Any auto-loaded command or any tool |
| command | string | :octicons-x-16: | Any command from the tool supplied as the previous argument |

## Keyword arguments

| Name | type | alias | info |
|------|------|----------|------|
| small | bool | -s | Displays the help page with less visual clutter |

## Examples

=== "Basic"
    ```shell
    help
    ```
    This shows all auto-loaded commands, and all loaded tools

=== "Tool"
    ```shell
    help system
    ```
    Show help for the loaded tool `system`

=== "Command"
    ```shell
    help help
    ```
    Show help for the command `help`

=== "Sub command"
    ```shell
    help system tree
    ```
    Show help for the command `tree` from the tool `system`