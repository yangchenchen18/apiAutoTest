'''
mark标记：
1.跳过用例，某个版本有缺陷导致脚本执行不通过，可以跳过该用例
2.脚本越来越多，如果想执行其中一部分，使用自定义标记
全量的脚本，挑选了、一部分作为冒烟测试的脚本，只想执行冒烟这部分的脚本

-m=smoke;
-m="smoke and api";
-m="smoke or api";
-m="not smoke";

'''
import pytest
@pytest.mark.smoke
def test_001():
    print("测试用例1")
@pytest.mark.skip("跳过的原因：尚未支持的功能，暂不执行")
def test_002():
    print("测试用例2")
def test_003():
    print("测试用例3")

@pytest.mark.api
def test_004():
    print("测试用例4")

class TestMark:
    @pytest.mark.smoke()
    def test_001(self):
        print("测试用例11")
    def test_002(self):
        print("测试用例12")

    @pytest.mark.smoke
    def test_003(self):
        print("测试用例13")
    def test_004(self):
        print("测试用例14")