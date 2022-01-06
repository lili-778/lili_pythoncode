import pytest


@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",35)])
def test_eval(test_input,expected):
    print(test_input,expected)

@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print(f"测试数据组合x：{x} y:{y}")