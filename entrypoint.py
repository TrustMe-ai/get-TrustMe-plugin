import sys
import json
import subprocess
import os
from enum import IntEnum


class SeverityKind(IntEnum):
    UNKNOWN = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    # TODO remove the below since they are not used
    CRITICAL = 4
    INFORMATIONAL = 5


def list_dirs_and_files(path):
    return [
        (entry,
         "Directory" if os.path.isdir(os.path.join(path, entry)) else "File")
        for entry in os.listdir(path)
    ]


print(sys.argv)


# path = sys.argv[1]
def validate_integer(value, name):
    try:
        return int(value)
    except ValueError:
        print(f"Error: {name} must be an integer. Provided value: '{value}'")
        sys.exit(1)


path = '/github/workspace'
# high_threshold = sys.argv[2]
# mid_threshold = sys.argv[3]
# low_threshold = sys.argv[4]

high_threshold = validate_integer(sys.argv[2], "fail-if-high-more-than")
mid_threshold = validate_integer(sys.argv[3], "fail-if-medium-more-than")
low_threshold = validate_integer(sys.argv[4], "fail-if-low-more-than")
token = sys.argv[5]


GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
GITHUB_REF_NAME = os.environ.get('GITHUB_REF_NAME')

output_file = '/scan/output.json'

command = f'python /engine/src/main.py fs {path} -o {output_file}'

if token:
    command = f'python /engine/src/main.py remote {path} --token={token} --repo-url=https://github.com/{GITHUB_REPOSITORY}.git --branch={GITHUB_REF_NAME} -o {output_file}'

print(command)

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True,
    cwd='/app',
    env={
        "SERVER_TYPE": "QA",
    },
)

print("returncode :- ", result.returncode)
print("stdout :- ", result.stdout)

if result.returncode != 0:
    print(result.stderr)
    sys.exit(1)

try:
    with open(output_file, 'r') as fp:
        results = json.load(fp)
    # print("Scan results:", json.dumps(results, indent=4))
except json.JSONDecodeError:
    print("Error: Failed to parse JSON output from the scanner.")
    print("Raw output:", result.stdout)
    sys.exit(1)
# results = json.loads(result.stdout)
# print(results)

if results['count']['total']['count']['3'] > high_threshold:
    print(
        f"Error: High vulnerabilities exceed the threshold ({high_threshold})."
    )
    exit(1)
if results['count']['total']['count']['2'] > mid_threshold:
    print(
        f"Error: Medium vulnerabilities exceed the threshold ({mid_threshold})."
    )
    exit(1)
if results['count']['total']['count']['1'] > low_threshold:
    print(
        f"Error: Low vulnerabilities exceed the threshold ({low_threshold}).")
    exit(1)

# os.environ['GITHUB_OUTPUT'] = str(result.stdout)
os.environ['GITHUB_OUTPUT'] = json.dumps(results)
print("Script completed successfully.")
