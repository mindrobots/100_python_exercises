# read the JSON format file into a dict
# 
# points 3

import json
from pprint import pprint

with open('company1.json','r') as f:
    d = json.load(f)

pprint(d)