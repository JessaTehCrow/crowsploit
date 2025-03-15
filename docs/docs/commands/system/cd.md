# Cd

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `module`

```shell
cd path?
```

description

## Arguments

| Name | Type | Default | Required | Info |
|------|------|---------|----------|------|
| `path` | string | Home | :octicons-x-16: | Changes the current work directory to the provided path (Or home directory if empty) |

## Extra

The provided path works like it would in linux.

- `./` is the current directory
- `..` is the previous directory
- `/` is from the root directory

## Examples

=== "basic"
    ```shell
    cd ..
    ```
    Change active directory to the parent of the current directory

    for example:
    `/root/Config` -> `/root`