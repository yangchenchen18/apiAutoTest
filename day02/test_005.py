'''
fixture的作用域
1.默认是函数级别的
2.函数级别-》模块级别—》类级别-》session级别
'''
import pytest
@pytest.fixture(scope='module')
def login():
    print("登录系统")
    yield #yiled之前是前置，之后是后置
    print("退出系统")
# 测试脚本
def test_query():
    print("查询功能，不需要登录")
def test_add(login):
    print("添加功能，需要登录") #第一次使用fixture的地方执行前置

def test_delete():
    print("删除功能，需要登录")
def test_modify():
    print("执行修改功能") #模块执行结束，执行后置
