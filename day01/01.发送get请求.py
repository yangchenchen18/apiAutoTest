import requests

# 发送一个请求，返回一个响应，将响应存到变量r中
# r = requests.get("http://www.baidu.com")
# print(r.text)

r = requests.get("http://192.168.150.54:8089//futureloan/mvc/api/member/list")
response = r.text
print(response)
print(r.json())
r = r.json()
assert r['status'] == 1
assert r['code'] == "10001"
# get请求带参数
r = requests.get(
    "http://192.168.150.54:8089//futureloan/mvc/api/member/register?mobilephone=13812345678&pwd=123456789012345678&regname=")
print(r.json())

r = r.json()
# assert r['status'] == 1
# assert r['code'] == "10001"
url = "http://192.168.150.54:8089//futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13556787456", "pwd": "123456", "regname": "hello"}

r = requests.get(url, params=user)
print(type(r))
r = r.json()
print(r)
# assert r['status'] == 1
# assert r['code'] == "10001"
# assert r['msg'] == "注册成功"

url="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
user={"tel":"13152156786"}
r=requests.get(url,params=user)

print(r.text)
print(type(r))
print(r.status_code)
print(r.reason)
print(r.cookies)
print(r.encoding)
print(r.headers)

# 发送请求时，带请求头
# 通过设置请求头。伪装成浏览器发的请求
# httpbin是一个测试网站，发送的请求，将返回json格式
url="http://www.httpbin.org/get?user=root&pwd=123456"
r=requests.get(url)
print(r.text)
head={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
r=requests.get(url,headers=head)
print(r.text)
