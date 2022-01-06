import pytest


@pytest.fixture()
def login():
    print("这个是登录方法")
    return ("tom","123")
@pytest.fixture()
def operate():
    print("登陆后的操作")
def test_case1(login,operate):
    print(login)
    print("test case1 ,需要登录")

def test_case2():
    print("test case2 ,不需要登录")

def test_case3(login):
    print("test case3 ,需要登录")
