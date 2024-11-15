import sys
import json
import subprocess

print(sys.argv)

path = sys.argv[1]

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
