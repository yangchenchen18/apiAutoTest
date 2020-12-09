import requests

url = "http://192.168.150.54:8089//futureloan/mvc/api/member/register"

try:
    data = {"Mobilephone": "13012345670", "pwd": "123456"}
    r = requests.post(url, data)
    assert r.json()['msg']=="成功"
    data = {"Mobilephone": "13112345679", "pwd": "123456789123456789"}
    r = requests.post(url, data)
    assert r.json()['msg']=="成功"
    data = {"Mobilephone": "13212345677", "pwd": "123456", "regname": "闪电"}
    assert r.json()['msg']=="成功"
    print(r.text)
    data = {"Mobilephone": "13312345674", "pwd": "123456789123456789", "regname": "闪电"}
    r = requests.post(url, data)
    assert r.json()['msg']=="成功"
except Exception as e:
    print(e)
data = {"pwd": "123456"}
r = requests.post(url, data)
assert r.json()['msg']=="参数错误：参数不能为空"
data = {"Mobilephone": " ", "pwd": "123456", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="参数错误：参数不能为空"
data = {"Mobilephone": "1315", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "1315", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "1315", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "131533547658", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "131533547658", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "131533547658", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "@1234567890", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "@1234567890", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "闪电123456789", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "闪电123456789", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "1123456789", "pwd": "1234567"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "1123456789", "pwd": "1234567", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码格式不正确"
data = {"Mobilephone": "13567890987", "pwd": "12345", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="密码长度必须为6~18"
data = {"Mobilephone": "13567890987", "pwd": "12345"}
r = requests.post(url, data)
assert r.json()['msg']=="密码长度必须为6~18"
data = {"Mobilephone": "13567890987", "pwd": "1234567890123456789", "regname": "闪电"}
r = requests.post(url, data)
assert r.json()['msg']=="密码长度必须为6~18"
data = {"Mobilephone": "13567890987", "pwd": "1234567890123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="密码长度必须为6~18"
data = {"Mobilephone": "13567890987", }
assert r.json()['msg']=="参数错误：参数不能为空"
print(r.text)
data = {"Mobilephone": "13567890987", "regname": "闪电"}
assert r.json()['msg']=="参数错误：参数不能为空"
print(r.text)
data = {"Mobilephone": "13012345678", "pwd": "123456"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码已被注册"
data = {"Mobilephone": "13112345678", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="手机号码已被注册"
print("===========================================")
url = "http://192.168.150.54:8089//futureloan/mvc/api/member/login"
data = {"Mobilephone": "13012345678", "pwd": "123456"}
r = requests.post(url, data)
assert r.json()['msg']=="成功"
data = {"Mobilephone": "13112345678", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="成功"
data = {"Mobilephone": " ", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="参数错误：参数不能为空"
data = {"Mobilephone": "1311", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="成功"
data = {"Mobilephone": "135678909821", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="用户名或者密码错误"
data = {"Mobilephone": "13567890981", "pwd": "123456789123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="用户名或者密码错误"
data = {"Mobilephone": "13567890981"}
r = requests.post(url, data)
assert r.json()['msg']=="参数错误：参数不能为空"
data = {"Mobilephone": "13567890981", "pwd": "12345"}
r = requests.post(url, data)
print(r.text)
data = {"Mobilephone": "13567890981", "pwd": "1234567890123456789"}
r = requests.post(url, data)
assert r.json()['msg']=="用户名或者密码错误"

