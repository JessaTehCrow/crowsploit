# Tree

```shell
system tree path? --raw
```

Displays a more visual representation of the system than ls.

## Arguments

| Name | Type | Default | Required | Info |
|------|------|---------|----------|------|
| `path` | type | Current Path | :octicons-x-16: | What path to start the tree from |

## Keyword arguments

| Name | Type | Default | Alias | Info |
|------|------|---------|-------|------|
| `raw` | bool | False | `-r` | Shows the final result without any fancy visuals (Used for piping) |

## Examples

=== "basic"
    ```shell
    system tree /root/
    ```
    Shows the system tree for the folder `/root`

    This could look something like the following:

    ```
    ——Г drwxr----- 3.29MB root root root
      |——Г drwxrwx--- 0MB root root Desktop
      |  | drwxrwx--- 32MB root root ScanLan.exe
      |
      |——Г drwxrwx--- 0MB root root Downloads
      |  | drwxrwx--- 0MB root root file.txt
      |
      |——Г drwxrwx--- 0MB root root Config
      |  | -rwxr-xr-x 0MB root root Mail.txt
    ```

=== "raw"
    ```shell
    system tree /root --raw
    ```
    Shows the system tree for the folder `/root`

    This could look something like the following:

    ```
    /root/Desktop
    /root/Desktop/ScanLan.exe
    /root/Downloads
    /root/Downloads/file.etxt
    /root/Config
    /root/Config/Mail.txt
    ```