#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export FLAVOUR='github'

echo "======= CLI Version ======="
echo "===========${GITHUB_TOKEN}================"
echo "===========${INPUT_HOST}================"