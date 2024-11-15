import json
import subprocess

command = '/app/dist/main'
result = subprocess.run(command, shell=True, capture_output=True, text=True)
results = json.loads(result.stdout)

print(results)
