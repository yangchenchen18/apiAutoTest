import pytest

from ZongHe.baw import Member, Dbop
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml(r"data_case\\register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"data_case\\register_success.yaml"))
def success_data(request):
    return request.param


def test_register_fail(fail_data, url, baserequests):
    print(f"测试数据：{fail_data}")
    r = Member.register(url, baserequests, fail_data["data"])
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['code'] == fail_data['expect']['code']

def test_register_pass(success_data,db, url, baserequests):

    print(f"测试数据：{success_data}")
    mobile=success_data['data']['mobilephone']
    Dbop.delete_user(db, mobile)
    r = Member.register(url, baserequests, success_data["data"])
    # assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['code'] == success_data['expect']['code']
    assert r.json()['status'] == success_data['expect']['status']
    r= Member.list(url, baserequests)
    print(r.json())
    assert mobile in r.text
    Dbop.delete_user(db, mobile)

def test_reregister_fail(success_data,db, url, baserequests):
    print(f"测试数据：{success_data}")
    mobile=success_data['data']['mobilephone']
    Dbop.delete_user(db, mobile)
    r = Member.register(url, baserequests, success_data["data"])
    # assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['code'] == success_data['expect']['code']
    assert r.json()['status'] == success_data['expect']['status']
    # r= Member.list(url, baserequests)
    # assert mobile in r.text
    r = Member.register(url, baserequests, success_data["data"])
    assert r.json()['msg']=="手机号码已被注册"
    assert r.json()['status'] ==0
    assert r.json()['code'] =="20110"
    Dbop.delete_user(db, mobile)
