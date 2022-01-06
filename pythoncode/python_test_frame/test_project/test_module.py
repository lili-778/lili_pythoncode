def setup_module():
    print("setup module")
def teardown_module():
    print("teardown module")
class TestDemo:
    def setup_class(self):
        print("TestDemo setup class")
    def teardown_class(self):
        print("TestDemo teardown class")
    def setup(self):
        print("类方法里的setup")
    def teardown(self):
        print("类方法里的teardown")
    def test_demo1(self):
        print("test demo1")
    def test_demo2(self):
        print("test demo2")

class TestDemo1:
    def test_demo3(self):
        print("test demo3")