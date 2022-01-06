import pytest


@pytest.fixture(scope="class",autouse=True)
def open():
    print("打开浏览器")
    yield
    print("执行teardown")
    print("最后关闭浏览器")
def test_ss():
    print("测试1")
class TestDemo:
    def test_search1(self):
        print("test search1")
        # raise NameError

    def test_search2(self):
        print("test search2")

    def test_search3(self):
        print("test search3")