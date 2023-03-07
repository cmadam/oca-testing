#!/bin/bash
CRT_DIR=${PWD}
source ${HOME}/huntingtest/huntingtest/bin/activate
cd ${HOME}/huntingtest
cp ${CRT_DIR}/elastictl-patch/import.go elastictl/tools/
cp ${CRT_DIR}/Dockerfile.build.elastictl elastictl
${CRT_DIR}/install-elastictl.sh
cd ${CRT_DIR}