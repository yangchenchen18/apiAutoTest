import requests
url="http://192.168.150.54:8089//futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13556787456", "pwd": "123456"}

r=requests.post(url,data=user)
print(r.text)
print(r.json())
print(r.status_code)
print(r.reason)
print(r.headers)

url="http://www.httpbin.org/post"
user = {
    "mobilephone": "13556787456", "pwd": "123456"}

r=requests.post(url,data=user)
print(r.text)
print("=============")
r=requests.post(url,json=user)
print(r.text)

url="http://192.168.150.54:8089//futureloan/mvc/api/member/recharge"
user={"mobilephone":"13556787456","amount":"50"}
r=requests.post(url,data=user)
print(r.text)
