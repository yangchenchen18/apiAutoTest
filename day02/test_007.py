
import pytest
@pytest.fixture(params=[{"username":"root","pwd":"123456"
                        },{"username":"admin","pwd":"888888"},
                        {"username":"administrator","pwd":"1233456"},"four"
               ,5 ])
def login_data(request):
    return request.param


def test_login(login_data):
    print(f"测试登录功能，测试数据为：{login_data}")
