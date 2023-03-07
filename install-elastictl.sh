#!/bin/bash

cd elastictl
export DOCKER_BUILDKIT=1
docker build --target bin --output bin/ -f Dockerfile.build.elastictl .
bin/elastictl e --help
