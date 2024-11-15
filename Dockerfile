# Container image that runs your code
FROM python:3.10

WORKDIR /app/

# ================================
# trivy
# ================================

RUN TA=$(arch | sed s/aarch64/ARM64/ | sed s/x86_64/64bit/) && \
wget https://github.com/aquasecurity/trivy/releases/download/v0.49.1/trivy_0.49.1_Linux-${TA}.deb \
&& dpkg -i trivy_0.49.1_Linux-${TA}.deb
# COPY .trivy/trivy.yaml /home/sbx_user1051/trivy.yaml

# ================================
# python
# ================================

RUN pip install bandit ruff

# ================================


COPY ./dist/ ./dist/

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
