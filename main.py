import sys
import json
import subprocess
import os


def list_dirs_and_files(path):
    return [
        (entry,
         "Directory" if os.path.isdir(os.path.join(path, entry)) else "File")
        for entry in os.listdir(path)
    ]


print(sys.argv)

# path = sys.argv[1]
path = '.'
high_threshold = sys.argv[2]
mid_threshold = sys.argv[3]
low_threshold = sys.argv[4]

print('cwd', os.getcwd())
print(list_dirs_and_files(path))

command = f'/app/dist/main {path}'
print(command)
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("exit code", result.returncode)
print("exit code", result.stdout)

if result.returncode != 0:
    print(result.stderr)
    sys.exit(1)

results = json.loads(result.stdout)
print(results)

if results['total']['HIGH'] > int(high_threshold):
    exit(1)
if results['total']['MEDIUM'] > int(mid_threshold):
    exit(1)
if results['total']['LOW'] > int(low_threshold):
    exit(1)
