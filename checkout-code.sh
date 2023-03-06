#!/bin/bash
CRT_DIR=${PWD}
mkdir -p ${HOME}/huntingtest
cd ${HOME}/huntingtest
git clone git@github.com:cmadam/stix-shifter.git
git clone git@github.com:cmadam/kestrel-lang.git
git clone git@github.com:subbyte/elastictl.git
cd ${CRT_DIR}
