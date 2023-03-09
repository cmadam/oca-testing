import base64
import os
import requests
import shlex
import subprocess
import sys
import time

print("Checking existence of the 'elastic' network")
proc1 = subprocess.run(shlex.split('docker network ls'), capture_output=True, encoding='utf-8')
docker_networks = proc1.stdout.split('\n')
elastic_net_found = False
for docker_net in docker_networks:
    net = docker_net.split()
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
    sys.exit(-1)

pwd_found = False
num_attempts = 1
while not pwd_found and num_attempts < 11:
    print(f"Attempt {num_attempts} to find password ...")
    proc4 = subprocess.run(shlex.split('docker logs es01'), capture_output=True,
                        encoding='utf-8')
    if proc4.returncode != 0:
        print(f"Failed to get logs for 'es01': error code {proc3.returncode}\n"
            f"{proc3.stderr}")
        sys.exit(-1)
    pwd_string = "Password for the"
    output_lines = proc4.stdout.split('\n')
    for ix, line in enumerate(output_lines):
        if pwd_string in line:
            pwd_found = True
            break
    time.sleep(5)
    num_attempts += 1
if not pwd_found:
    print(f"Could not find password in the logs after {num_attempts} tries")
    sys.exit(-1)
else:
    log_pwd = str(output_lines[ix + 1].encode('utf-8', errors='ignore').strip())
    tokens = log_pwd.split('\\x1b[')
    print(tokens)
    pwd = tokens[1][2:]
pwd_file_name = os.path.join(os.getenv('HOME'), '.es_pwd')
with open(pwd_file_name, 'w') as f:
    f.write(pwd)

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
            print(f"Attempt {attempts} to ping elastic server")
            attempts += 1
            time.sleep(5)
    except:
        print(f"Attempt {attempts} to ping elastic server after failing to connect")
        attempts += 1
        time.sleep(5)
if elastic_ready:
    print(f"Elastic server ready after {attempts} attempts")
else:
    print(f"Gave up after {attempts} attempts")
    sys.exit(-1)
