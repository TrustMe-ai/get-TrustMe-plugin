ARG BASE_IMAGE=ghcr.io/trustme-ai/scan-engine:latest
ARG SERVER_TYPE=PROD

FROM ${BASE_IMAGE} as base

ENV SERVER_TYPE=${SERVER_TYPE}

WORKDIR /app/

# # Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py ./entrypoint.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
# ENTRYPOINT ["/entrypoint.sh"]
ENTRYPOINT ["python", "/app/entrypoint.py"]
