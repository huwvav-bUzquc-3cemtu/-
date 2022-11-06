import requests
import time
import pandas as pd
import random
import os
import json
# 定义爬取函数
def get_pdf_address(pageNum,start_date,end_date):
    url = 'http://www.szse.cn/api/disc/announcement/annList?random=%s' % random.random()
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01'
    ,'Accept-Encoding': 'gzip, deflate'
    ,'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    ,'Content-Type': 'application/json'
    ,'Host': 'www.szse.cn'
    ,'Origin': 'http://www.szse.cn'
    ,'Proxy-Connection': 'keep-alive'
    ,'Referer': 'http://www.szse.cn/disclosure/listed/fixed/index.html'
    ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    ,'X-Request-Type': 'ajax'
    ,'X-Requested-With': 'XMLHttpRequest'}
    pagenum = int(pageNum)
    payload = {"seDate":["{}-12-31".format(start_date),"{}-12-31".format(end_date)],"channelCode":["fixed_disc"],"bigCategoryId":["010301"],"pageSize":30,"pageNum":pagenum}
    r = requests.post(url,headers = headers,data = json.dumps(payload))
    result = r.json()
    return result

answer = get_pdf_address(20,2020,2021)
with open ('ans.json','w') as f:
    json.dump(answer,f)
    