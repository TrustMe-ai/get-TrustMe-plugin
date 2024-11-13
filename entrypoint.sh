#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export FLAVOUR='github'

echo "======= CLI Version ======="
# echo "===========${GITHUB_TOKEN}================"
if [ "$INPUT_HOST" = "dead" ]; then
    echo "Environment variable STATUS is 'dead'. Exiting with code 1."
    exit 1
else
    echo "Environment variable STATUS is not 'dead'. Exiting with code 0."
    exit 0

fi
echo "===========${INPUT_HOST}================"