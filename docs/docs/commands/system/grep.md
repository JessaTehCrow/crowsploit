# Grep

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `module`

```shell
grep pattern rest --invert --regex --ignore-case --highlight --isolate --no-color
```

Filter data based on patterns.

## Arguments

| Name | Type | Default | Required | Info |
|------|------|---------|----------|------|
| `pattern` | string | None | :octicons-check-16: | What pattern to look for |
| `rest` | string | None | :octicons-check-16: | Data to find patterns in (Mostly supplied through piping)|

## Keyword arguments

| Name | Type | Default | Alias | Info |
|------|------|---------|-------|------|
|`invert` | bool | False | `-v` | DON'T match the pattern |
|`regex` | bool | False | `-e` | Use regex for mattern recognition |
|`ignore-case` | bool | False | `-i` | Ignore capitalization in the data |
|`highlight` | bool | False | `-h` | Highlihgt what matched the pattern |
|`isolate` | bool | False | `-s` | Only display what matched the pattern and cut everything else |
|`no-color` | bool | False | `-c` | Remove color |

## Examples

=== "basic"
    ```shell
    command thing
    ```
    description thing