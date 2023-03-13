#!/bin/bash
CRT_DIR="${PWD}"
mkdir -p "${HOME}"/huntingtest
cd "${HOME}"/huntingtest || exit
git clone git@github.com:cmadam/stix-shifter.git
git clone git@github.com:cmadam/kestrel-lang.git
cd "${CRT_DIR}" || exit
