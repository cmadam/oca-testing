#!/bin/bash

echo "docker network create elastic"
docker network create elastic
echo "Created 'elastic' docker network"

echo "docker run -d --name es01test -e ES_JAVA_OPTS=\"-Xms1g -Xmx1g\" -e \"discovery.type=single-node\" --net elastic -p 9234:9200 -it docker.elastic.co/elasticsearch/elasticsearch:8.6.2"
docker run -d --name es01test -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -e "discovery.type=single-node" --net elastic -p 9234:9200 -it docker.elastic.co/elasticsearch/elasticsearch:8.6.2
pip install requests
python setup_elastic.py

echo "docker exec -it es01test bash -c \"bin/elasticsearch-reset-password -u elastic -s -b\""
docker exec es01test bash -lc "bin/elasticsearch-reset-password -u elastic -s -b" > "${HOME}"/.es_pwd

python setup_elastic.py --secure