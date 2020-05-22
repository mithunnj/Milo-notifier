import json


with open('outbound_num.json') as json_file:
    data = json.load(json_file)
    print(data)
