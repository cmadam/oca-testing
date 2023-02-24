import base64
import json
import os
import requests
import yaml

config_file = os.path.join(
    os.getenv('HOME'),
    '.config',
    'kestrel',
    'stixshifter.yaml'
)
with open(config_file, 'r') as fp:
    config = yaml.safe_load(fp)
test_config = config.get('profiles', {}).get('testdata', {})
headers = {}
auth = test_config.get('config', {}).get('auth', {})
headers['Authorization'] = b'ApiKey ' + base64.b64encode((
    f"{auth['id']}:{auth['api_key']}").encode('ascii'))
headers['Content-Type'] = 'application/json'
url = f"https://{test_config['connection']['host']}:" \
    f"{test_config['connection']['port']}/" \
    f"{test_config['connection']['indices']}/_search"
# data = '{"query": {"match": "process.command_line.keyword : \\"C:\\\\\\\\Windows\\\\\\\\system32\\\\\\\\svchost.exe -k netsvcs -p -s Schedule\\" OR powershell.command.value : \\"C:\\\\\\\\Windows\\\\\\\\system32\\\\\\\\svchost.exe -k netsvcs -p -s Schedule\\") AND (@timestamp:[\\"2022-01-17T12:00:00.000Z\\" TO \\"2022-10-18T00:00:00.000Z\\"])"}}}'
data = {
    "query": {
        "match": {
            "process.command_line.keyword": "C:\\Windows\\system32\\svchost.exe -k netsvcs -p -s Schedule"
        }
    }
}
data = json.dumps(data)
res = requests.get(url, data=data, headers=headers, verify=False)
if res.status_code == 200:
    print(f'{res.status_code}:\n{json.dumps(res.json(), indent=2)}')
else:
    print(f'{res.status_code}: {res.text}')