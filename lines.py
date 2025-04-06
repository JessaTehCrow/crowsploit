import os

exclude = [
    "build",
    "docs",
    ".git",
    "unfinished_tools",
    "temp_tools",
    ".gitignore",
    "payload_parser"
]

lines = 0
chars = 0
tabless = 0

def get_files(path:str):
    files = []
    folders = []
    new = []
    for x in exclude:
        if path.endswith(x): 
            # print("\x1b[0;31m- ", path)
            return []

    print("\n\x1b[0;34m"+path+"\x1b[0m")
    for f in os.listdir(path):
        if os.path.isdir(path+ "/"+f):
            folders.append(path+"/"+f)
            # files += get_files(path+"/"+f)
        else:
            files.append(path+"/"+f)
            new.append(f)
    print("\x1b[0;32m+ "+"\x1b[0m, \x1b[0;32m".join(new)+"\x1b[0m")

    for f in folders:
        files += get_files(f)

    return files

files = get_files(os.getcwd())

for file in files:
    with open(file, "r") as f:
        temp = [x for x in f.readlines() if x != ""]
        lines += len(temp)
        chars += len("\n".join(temp))
        tabless += len("\n".join([x.strip() for x in temp]))

print()
print("\x1b[0mFile count: \x1b[0;33m", len(files))
print("\x1b[0mLines written: \x1b[0;33m", lines)
print("\x1b[0mTotal characters:\x1b[0;33m", chars)
print("\x1b[0mTotal characters without indentation:\x1b[0;33m", tabless)
print()