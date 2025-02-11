FROM ghcr.io/trustme-ai/scan-engine:latest

WORKDIR /app/

# # Copies your code file from your action repository to the filesystem path `/` of the container
# COPY entrypoint.sh /entrypoint.sh
COPY entrypoint.py ./entrypoint.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
# ENTRYPOINT ["/entrypoint.sh"]
ENTRYPOINT ["python", "/app/entrypoint.py"]
