import sys
import json
import subprocess

print(sys.argv)

command = '/app/dist/main'
result = subprocess.run(command, shell=True, capture_output=True, text=True)

if result.returncode != 0:
    print(result.stderr)

results = json.loads(result.stdout)

print(results)