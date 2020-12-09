import pytest
import requests


@pytest.fixture(params=[{"data":{"Mobilephone": "13012345678", "pwd": "123456"}, "except": {"msg":"手机号码已被注册"}},
                        {"data": {"pwd": "123456"},"except": {"msg":"参数错误：参数不能为空"}},
                        {"data": {"Mobilephone": "13912345678"},"except": {"msg":"参数错误：参数不能为空"}},
                        {"data":{"Mobilephone": "1315", "pwd": "1234567"},"except": {"msg":"手机号码格式不正确"}},
                        {"data":{"Mobilephone": "1315", "pwd": "1234567", "regname": "闪电"},"except": {"msg":"手机号码格式不正确"}},
                        {"data":{"Mobilephone": "13567890987", "pwd": "12345"},"except": {"msg":"密码长度必须为6~18"}}])
def register_data(request):
    return request.param


def test_register(register_data):
    url = "http://192.168.150.54:8089//futureloan/mvc/api/member/register"
    r = requests.post(url, register_data["data"])

    # print("预期结果",register_data["except"])
    assert r.json()['msg']==register_data["except"]['msg']
