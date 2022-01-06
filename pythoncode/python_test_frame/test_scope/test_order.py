import pytest


class Testpytst:
    @pytest.mark.run(order=-2)
    def test_one(self):
        print("test one 测试用例")

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test two 测试用例")

    @pytest.mark.run(order=-3)
    def test_three(self):

        print("test three 测试用例")