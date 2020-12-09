'''
fixture 测试前置和后置，比较常用的方式
1.命名比较灵活，不限于setup、teardown等命名方式
2.使用比较灵活
3.不需要import即可实现共享
'''
import pytest
@pytest.fixture(scope='module')
def login():
    print("登录成功")
    yield #yiled之前是前置，之后是后置
    print("退出登录")

@pytest.fixture(scope='module')
def db():
    print("连接数据库")
    yield #yiled之前是前置，之后是后置
    print("断开数据库连接")

def test_query(db):
    print("执行查询功能，不需要登录")
def test_add(login,db):
    print("添加功能，需要登录")
@pytest.mark.usefixtures("login")
def test_delete():
    print("删除功能，需要登录")