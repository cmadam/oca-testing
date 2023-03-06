#!/bin/bash

echo "docker network create elastic"
docker network create elastic
echo "Created 'elastic' docker network"
echo "docker run -d --name elastic-search --net elastic -p 9200:9200 -p 9300:9300 -e \"discovery.type=single-node\" elasticsearch:7.17.8"
docker run -d --name elastic-search --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.17.8
echo "Created 'elastic' instance"
sleep 5
echo "docker ps -a"
docker ps -a
