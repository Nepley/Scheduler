import requests
import time
import json
from datetime import datetime

url = "http://Nepgeardam:80/scheduler"
url_exec = "http://Nepgeardam:80/scheduler/exec"

while True:
    time.sleep(1)
    actions = json.loads(requests.request("GET", url).text)
    now = datetime.now()
    for action in actions:
        if datetime.fromisoformat(action['next_call']) <= now:
            requests.request("GET", url_exec+"?manual=False&id="+action['_id'])