#!/bin/bash

ES_PWD=$(cat "${HOME}"/.es_pwd)
cp config/kestrel-stixshifter-config.yml "${HOME}"/huntingtest/kestrel-stixshifter-config.yaml
sed -i "s/<ES_PWD>/${ES_PWD}/" "${HOME}"/huntingtest/kestrel-stixshifter-config.yaml
export KESTREL_STIXSHIFTER_CONFIG=${HOME}/huntingtest/kestrel-stixshifter-config.yaml
kestrel huntbooks/kestrel-test.hf
