import pytest

from ZongHe.baw import Dbop, Member
from ZongHe.caw import DataRead


@pytest.fixture(scope="module",params=DataRead.read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param
@pytest.fixture(scope="module",params=DataRead.read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(scope='module')
def register(setup_data,db, url, baserequests):
    mobile = setup_data['casedata']['mobilephone']
    Dbop.delete_user(db, mobile)
    Member.register(url, baserequests, setup_data["casedata"])
    yield
    Dbop.delete_user(db, mobile)

def test_login(register,url,baserequests,login_data):
    r=Member.login(url,baserequests,login_data["casedata"])
    assert r.json()['code']==login_data['expect']['code']
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['status'] == login_data['expect']['status']