'''
pytest是一种测试框架，用来方便的组织测试脚本、生成报告、或者与其他工具集成
1.测试文件以test_开头或_test结尾
2.测试类以Tset开头
3.测试函数、方法以test_开头
'''
import requests
url = "http://192.168.150.54:8089//futureloan/mvc/api/member/register"
def test_register_001():
    data = {"Mobilephone": "13012345678", "pwd": "123456"}
    r=requests.post(url,data)
    assert r.json()['msg']=="成功"
def test_register_002():
    data = {"Mobilephone": "13112345678", "pwd": "123456789123456789"}
    r=requests.post(url,data)
    assert r.json()['msg']=="成功"


def test_register_003():
    data = {"Mobilephone": "13212345678", "pwd": "123456", "regname": "闪电"}
    r = requests.post(url, data)
    # assert r.json()['msg'] == "成功"

def test_register_004():
    data = {"Mobilephone": "1123456789", "pwd": "1234567"}
    r = requests.post(url, data)
    assert r.json()['msg'] == "手机号码格式不正确"

def test_register_005():
    data = {"Mobilephone": "闪电123456789", "pwd": "1234567", "regname": "闪电"}
    r = requests.post(url, data)
    assert r.json()['msg'] == "手机号码格式不正确"
def test_register_006():
    data = {"Mobilephone": "@1234567890", "pwd": "1234567"}
    r = requests.post(url, data)
    assert r.json()['msg'] == "手机号码格式不正确"


