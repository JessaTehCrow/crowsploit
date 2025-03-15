# History

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `module`

```shell
history --limit --clear
```

Shows the command history for the current session

## Keyword arguments

| Name | Type | Default | Alias | Info |
|------|------|---------|-------|------|
| `limit` | int | 10 | `-l` | The amount of commands to show |
| `clear` | bool | False | | Clears the command history of the current session |

## Examples

=== "basic"
    ```shell
    command thing
    ```
    description thing