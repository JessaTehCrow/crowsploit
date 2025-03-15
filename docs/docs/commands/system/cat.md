# Cat

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `module`

```shell
cat file --format --force
```

Displays the content of a file to the terminal

## Arguments

| Name | Type | Required | Info |
|------|------|----------|------|
| file | string | :octicons-check-16: | A file on the current system |

## Keyword arguments

| Name | Type | Default | Alias | Info |
|------|------|---------|-------|------|
| `format` | bool | False | `-m` | Adds syntax highlighting to the printed output |
| `force` | bool | False | `-f` | Attempts to force output from a file even without permissions |

!!! note
    the `--force` argument tends to only work for `/etc/passwd`.
    However, other files may also be vulnerable to this.
    So long as a file does not have `"` or `'` characters in them, this should work.

!!! note
    Formatting is automatically applied to any `.src` file

## Examples

=== "basic"
    ```shell
    cat Mail.txt
    ```
    Display the content of `Mail.txt` in the current directory

===  "Formatting"
    ```shell
    cat /etc/Sources.txt -m
    ```
    Display the content of `/etc/Sources.txt` and apply syntax highlighting to the output

=== "Forcing output"
    ```shell
    cat /etc/passwd -f
    ```
    Force the system to display the content of `/etc/passwd`

    !!! warning ""
        This creates two new files. Since this is using an `import_code` method.
        - catthing.src
        - catthing