import requests

s = requests.Session()
url = "http://114.67.246.176:17548/"
res = s.get(url)
value = eval(res.text.split("<div>")[1].split("=")[0])
data = {"value":value}

flag = s.post(url, data=data)
print(flag.text)
