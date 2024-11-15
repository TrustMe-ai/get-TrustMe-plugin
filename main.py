import sys
import json
import subprocess
from pathlib import Path

def list_dirs_and_files(path):
    return [(entry.name, "Directory" if entry.is_dir() else "File") for entry in Path(path).iterdir()]


print(sys.argv)

path = sys.argv[1]

print(list_dirs_and_files(path))

command = f'/app/dist/main {path}'
print(command)
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("exit code", result.returncode)
print("exit code", result.stdout)

if result.returncode != 0:
    print(result.stderr)
    sys.exit(1)

# results = json.loads(result.stdout)

# print(results)
