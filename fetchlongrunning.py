import os
import json
import requests
import csv
import sys
from subprocess import run
if os.path.exists("/tmp/appdata.csv"):
  os.remove("/tmp/appdata.csv")
else:
  print("The file does not exist")
searchurl = 'http://localhost:4171/{}/_search'.format(sys.argv[1])
payload = {"query":{"bool":{"must":[{"term":{"status":"R"}},{"range":{"duration":{"gte":22000}}}]}}}
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(searchurl, data=json.dumps(payload), headers=headers)
hitsdata=r.json()['hits']['hits']
for i in range(len(hitsdata)):
    app_id=hitsdata[i]['_source']['id']
    stat_time=hitsdata[i]['_source']['startTime']
    app_duration=round((hitsdata[i]['_source']['duration'])/3600000,2)
    data = [app_id, stat_time, app_duration]
    with open('/tmp/appdata.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(data)
