# append a record to the JSON file
# 
# points 3

import json

with open('company1.json','r+') as f:
    d = json.load(f)
    d['employees'].append({'firstname':'Albert','lastName':'Bert'})
    f.seek(0)
    json.dump(d, f, indent=4, sort_keys=True)
    f.truncate()
    