import json
with open("dummydataTask.json", "r") as fin:
    data = json.load(fin)
for a in data:
    print(a['id'])
    