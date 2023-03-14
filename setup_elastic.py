import base64
import os
import requests
import shlex
import subprocess
import sys
import time

# setup 'elastic' docker network
print("Checking existence of the 'elastic' network")
proc1 = subprocess.run(shlex.split('docker network ls'), capture_output=True, encoding='utf-8')
docker_networks = proc1.stdout.split('\n')
elastic_net_found = False
for docker_net in docker_networks:
    net = docker_net.split()
    if len(net) < 2:
        continue
    if net[1] == 'elastic':
        elastic_net_found = True
        break
if elastic_net_found:
    print("Found 'elastic' docker network")
else:
    print("'elastic' docker network not found, creating")
    try:
        proc2 = subprocess.run(shlex.split('docker network create elastic'),
                               check=True)
        print("'elastic' docker network successfully created")
    except:
        print(f"Failed to create 'elastic' docker network: "
              f"error code {proc2.returncode}, error message: {proc2.stderr}")
        sys.exit(-1)

# launch elasticsearch docker instance
print("Launching elasticsearch docker instance")
proc3 = subprocess.run(
    shlex.split('docker run -d --name es01 -e ES_JAVA_OPTS="-Xms1g -Xmx1g" '
                '-e "discovery.type=single-node" --net elastic -p 9200:9200 -it '
                'docker.elastic.co/elasticsearch/elasticsearch:8.6.2'),
    capture_output=True,
    encoding='utf-8'
)
if proc3.returncode != 0:
    print(f"Failed to create elasticsearch docker instance 'es01': "
          f"error code {proc3.returncode},\n{proc3.stderr}")
    # sys.exit(-1)

# setup elasticsearch password
pwd = None
proc4 = subprocess.run(shlex.split(
    'docker exec -it es01 bash -c "bin/elasticsearch-reset-password '
    '-u elastic -s -b"'), capture_output=True, encoding='utf-8')
if proc4.returncode != 0:
    print(f"Failed to get logs for 'es01': error code {proc4.returncode}\n"
          f"{proc4.stderr}")
    sys.exit(-1)
pwd = proc4.stdout.strip()
pwd_file_name = os.path.join(os.getenv('HOME'), '.es_pwd')
with open(pwd_file_name, 'w') as f:
    f.write(pwd)

# proceed after elasticsearch passes healthcheck
elastic_ready = False
localhost_url = 'https://localhost:9200'
attempts = 1
headers = {}
headers['Authorization'] = b"Basic " + base64.b64encode(f'elastic:{pwd}'.encode('ascii'))
while not elastic_ready and attempts <= 20:
    try:
        res = requests.get(localhost_url, headers=headers, verify=False)
        print(f"{res.status_code}: {res.text}")
        if res.status_code == 200:
            elastic_ready = True
        else:
            attempts += 1
            print(f"Attempt {attempts} to ping elastic server")
            time.sleep(5)
    except:
        attempts += 1
        print(f"Attempt {attempts} to ping elastic server after failing to connect")
        time.sleep(5)
if elastic_ready:
    print(f"Elastic server ready after {attempts} attempts")
else:
    print(f"Gave up after {attempts} attempts")
    sys.exit(-1)