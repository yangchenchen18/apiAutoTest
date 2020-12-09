'''
mock:
1.接口测试的测试场景比较难模拟，需要大量的工作才能做好
2.该接口的测试，依赖其他模块的接口，依赖的接口尚未开发完成
测试条件不充分时，怎么开展接口测试
使用mock模拟接口的返回值
'''
from unittest import mock

'''
支付接口：http://www.zhifu.com
方法：post
参数：{"订单号":"123456","支付金额":"20.56","支付方式":"支付宝/微信/余额"}
返回值：{"",""}
'''
import requests
class Pay:
    def zhifu(self,data):
        r=requests.post("http://www.zhifu.com",data=data)
        return r.json()

def test_001():
    pay=Pay()
    pay.zhifu=mock.Mock(return_value={"code":200,"msg":"支付成功"})
    canshu={"订单号":"123456","支付金额":"20.56","支付方式":"支付宝"}
    r=pay.zhifu(canshu)
    print(r)
    assert r['msg']=="支付成功"

def test_002():
    pay = Pay()
    pay.zhifu = mock.Mock(return_value={"code": 201, "msg": "支付失败"})
    canshu = {"订单号": "123456", "支付金额": "-20.56", "支付方式": "微信"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "支付失败"
@mock.patch("test_001.Pay.zhifu",return_value={"code": 201, "msg": "支付成功"})
def test_003(mock_pay):
    pay = Pay()
    # pay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
    canshu = {"订单号": "123456", "支付金额": "20.56", "支付方式": "支付宝"}
    r = pay.zhifu(canshu)
    print(r)
    assert r['msg'] == "支付成功"

def quxian(url,data):
    r=requests.get(url,data=data)
    return r.json()

def test_quxian():
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/withdraw"
    data = {"mobilephone": "13567891234", "amount": 150}
    quxian=mock.Mock(return_value={"status": 1, "code": 10001, "msg": "成功"})
    r = quxian(url, data)
    print(r)
    assert r['msg'] == "成功"