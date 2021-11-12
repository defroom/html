import requests
import base64

s = requests.Session()
url = "http://114.67.246.176:14953"
res = s.get(url)
txt = res.headers['flag']
key = base64.b64decode(txt).decode()[-8:]
num = base64.b64decode(key)
data = {'margin': num}
flag = s.post(url, data=data)
print(flag.text)