import requests
s=requests.session()

# 登录百格
url="https://www.bagevent.com/user/login"
data={
"access_type": "1",
"loginType": "1",
"emailLoginWay": "0",
"account": "2780487875@qq.com",
"password": "qq2780487875",
"remindmeBox": "on",
"remindme": "1"

}
print("登录前的cookies:",s.cookies)
r=s.post(url,data=data)
# print(r.text)
url="https://www.bagevent.com/account/dashboard"
r=s.get(url)
print(r.text)
assert '<div class="text">返回顶部</div>' in r.text
print("登录后的cookies:",s.cookies)
url="https://www.bagevent.com/user/login_out"
r=s.get(url)
print("退出后的cookies:",s.cookies)

url="https://www.bagevent.com/account/dashboard"
r=s.get(url)
# print(r.text)

print(s.cookies)