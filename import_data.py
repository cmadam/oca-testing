"""Check that elastic server is up and running before uploading data
to the server. Give up after 20 unsuccessful attempts to reach the
server. TODO: start elastictl from this program, once the server is up

"""
import json
import requests
import time

elastic_ready = False
localhost_url = 'http://localhost:9200'
attempts = 1
while not elastic_ready and attempts <= 20:
    try:
        res = requests.get(localhost_url)
        print(f"{res.status_code}: {res.text}")
        if res.status_code == 200:
            elastic_ready = True
        else:
            attempts += 1
            print(f"Attempt {attempts} to ping elastic server")
            time.sleep(10)
    except:
        attempts += 1
        print(f"Attempt {attempts} to ping elastic server after failing to connect")
        time.sleep(10)
if elastic_ready:
    print(f"Elastic server ready after {attempts} attempts")
else:
    print(f"Gave up after {attempts} attempts")

index_name = 'test-ecs'
datafile_name = 'test-ecs.data'
headers = {}
headers['Content-Type'] = 'application/json'
with open(datafile_name, 'r') as fp:
    for line_number, line in enumerate(fp):
        if line_number == 0:
            index_create_url = f"{localhost_url}/{index_name}"
            index_create_data = json.dumps(json.loads(line))
            res1 = requests.put(index_create_url, headers=headers)
            if res1.status_code in [200, 201]:
                print(f"{res1.status_code}: index {index_name} "
                      f"successfully created: {res1.text}")
            else:
                print(f"{res1.status_code}: failed to create {index_name} - "
                      f"{res1.text}")
        else:
            record = json.loads(line)
            record_index = record.get('_index')
            record_type = record.get('_type')
            record_id = record.get('_id')
            record_source = record.get('_source')
            if not record_index or not record_type or not record_id:
                print(f"Skipping doc {line_number}: "
                      f"index {record_index if record_index else 'missing'}, "
                      f"type {record_type if record_type else 'missing'}, "
                      f"id {record_id if record_id else 'missing'}")
                continue
            record_url = f"{localhost_url}/{record_index}/{record_type}/{record_id}"
            record_res = requests.put(record_url, headers=headers, data=json.dumps(record_source))
            if record_res.status_code in [200, 201]:
                print(f'Successfully added record {line_number}')
            else:
                print(f'Failed to add record {line_number}, {record_res.status_code} - {record_res.text}')
