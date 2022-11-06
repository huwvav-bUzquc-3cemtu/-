import json
filename = 'ans.json'
with open(filename) as f:
    all_data = json.load(f)
readable_file = 'ans_read.json'
with open(readable_file,'w') as f:
    json.dump(all_data,f,indent = 4)
