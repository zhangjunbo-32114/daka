import requests
from urllib.parse import urlencode
import json

url = 'https://www.dmuisatc.com/DMU_WEB/student_5/info/?'
headers = {
    'Host': 'www.informationofdum.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx8a86613d14cbe10c/10/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}

datas = []
datas4 = [
{
    "jsonnumber": "1120201469",
    "jsonname": "张竣博",
    "jsonclass": "2020级硕士研究生中队",
    "morning": "36.2℃",
    "afternoon": "36.2℃",
    "night": "36.2℃",
    "jsonbody": 1,
    "jsonbodychangeinfo": "",
    "textarea": "学校",
    "textprople": "同学",
    "jsontouch": 1,
    "jsontouchchangeinfo": 0,
    "jsonisolate": 1,
    "jsonisolatechangeinfo": 0,
    "latitude": 38.8664,
    "longitude": 121.5295,
}
]

for i in range(len(datas4)):
    datas.append(datas4[i])

for data in datas:
    url = 'www.informationofdum.com/DMU_WEB/student_5/info/?'
    url = url + urlencode(data)
    print(url)
    daka = requests.get(url, headers=headers)
    print(daka.text)


# headers = {"Authorization": "JWT Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"}

# #
#
# daka = requests.get(url, data=datas)
# print(daka)

