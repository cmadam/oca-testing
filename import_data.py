"""Check that elastic server is up and running before uploading data
to the server. Give up after 20 unsuccessful attempts to reach the
server. TODO: start elastictl from this program, once the server is up

"""
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
