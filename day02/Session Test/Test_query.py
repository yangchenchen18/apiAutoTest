class TestQuery():
    # 每个类执行一次，在第一次使用的地方执行前置，在类结束时执行后置
    def test_001(self):
        print("查询：用例1")
    def test_002(self,login):
        print("查询：用例2")
    def test_003(self,login):
        print("查询：用例4")
    def test_004(self,login):
        print("查询：用例5")