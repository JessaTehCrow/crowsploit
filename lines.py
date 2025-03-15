import os

exclude = [
    "build",
    "docs"
]

lines = 0
chars = 0
tabless = 0

def get_files(path:str):
    files = []
    for x in exclude:
        if path.endswith(x): return []

    for f in os.listdir(path):
        if os.path.isdir(path+ "/"+f):
            files += get_files(path+"/"+f)
        else:
            files.append(path+"/"+f)
    return files

files = get_files(os.getcwd())

for file in files:
    with open(file, "r") as f:
        temp = [x for x in f.readlines() if x != ""]
        lines += len(temp)
        chars += len("\n".join(temp))
        tabless += len("\n".join([x.strip() for x in temp]))

print("Lines written: ", lines)
print("Total characters:", chars)
print("Total characters without indentation:", tabless)