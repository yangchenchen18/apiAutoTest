'''
脚本层的一些公关方法
'''
import pytest

from ZongHe.caw import DataRead
from ZongHe.caw.BaseRequests import BaseRequests


@pytest.fixture(scope="session")
def url():
    return DataRead.read_ini('data_env/env.ini',"url")

@pytest.fixture(scope="session")
def baserequests():
    return BaseRequests()
@pytest.fixture(scope="session")
def db():
    info=DataRead.read_ini('data_env/env.ini',"db")
    return eval(info)#将字符串解析成字典