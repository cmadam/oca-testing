#!/bin/bash
CRT_DIR=${PWD}
source ${HOME}/huntingtest/huntingtest/bin/activate
cd ${HOME}/huntingtest
cp ${CRT_DIR}/Dockerfile.build.elastictl elastictl
${CRT_DIR}/install-elastictl.sh
cd ${CRT_DIR}