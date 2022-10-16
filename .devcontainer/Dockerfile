# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONPATH /workspaces/webhook-tester

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
