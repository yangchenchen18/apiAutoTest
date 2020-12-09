import pytest
'''
fixture作用域：session级别
公共方法放到conftest.py 文件中，文件名不能写错
整个执行过程，开始前执行前置，所有执行完了之后再执行
1.conftest文件可以存多个
2.conftest放在sessionTest目录下，对sessionTestxoad的py文件以及子目录下的py文件生效
3.conftest放到apiautotest目录下，对整个工程生效
4.不用import


'''
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出系统")
