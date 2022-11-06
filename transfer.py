import json
filename = 'ans_read.json'
filepath = 'datas.txt'
a = []
with open(filename) as f:
    all_data = json.load(f)
len = len(all_data['data'])
for i in range(0,len):
    a=[]
    ids = all_data['data'][i]['id']
    annids = all_data['data'][i]['annId']
    titles = all_data['data'][i]['title']
    publishTimes = all_data['data'][i]['publishTime']
    attachPaths = all_data['data'][i]['attachPath']
    attachFormats = all_data['data'][i]['attachFormat']
    attachSizes = all_data['data'][i]['attachSize']
    secCodes = ''.join(str(k) for k in all_data['data'][i]['secCode'])
    secNames = ''.join(str (k) for k in all_data['data'][i]['secName'])
    index = all_data['data'][i]['_index']
    a.append("id: "+ids)
    a.append(f"annid: {annids}")
    a.append("title: "+titles)
    a.append(publishTimes)
    a.append(attachPaths)
    a.append( attachFormats)
    a.append(f"{attachSizes}")
    a.append(secCodes )
    a.append(secNames)
    a.append(index)
    a.append('')
    print(a)
    for j in range (0,11):
        with open(filepath,'a') as file:
            file.write(a[j])
            file.write("\n")


