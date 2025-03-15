# Ls

!!! info
    This command is auto loaded.
    That means you can run this without needing to prefix it with `module`

```shell
ls path? --long --all --longall
```

Shows the files and folders that are inside of a folder.

## Arguments

| Name | Type | Default | Required | Info |
|------|------|---------|----------|------|
| `path` | string | Current Path | :octicons-x-16: | What folder to use |

## Keyword arguments

| Name | Type | Default | Alias | Info |
|------|------|---------|-------|------|
| `long` | bool | False | `-l` | Shows the file/folder permisions and filesize |
| `all` | bool | False | `-a` | Shows all files and folders, even if hidden |
| `longall` | bool | False | `-la` | Uses both `--long` and `--all` |

## Examples

=== "basic"
    ```shell
    ls
    ```
    Shows folders and files in the current directory

=== "Other folder"
    ```shell
    ls /etc
    ```
    Shows folders and files in the `/etc` folder

=== "Long"
    ```shell
    ls -l
    ```
    Shows all files and folders with the permission and filesize info

=== "All"
    ```shell
    ls -a
    ```
    Shows all hidden and unhidden folders / files

=== "Longall"
    ```shell
    ls -la
    ```
    Shows all hidden files, file sizes and also the permissions 