#!/bin/bash
CRT_DIR=${PWD}
source ${HOME}/huntingtest/huntingtest/bin/activate
cd ${HOME}/huntingtest
${CRT_DIR}/install-stix-shifter-kestrel.sh
cd ${CRT_DIR}