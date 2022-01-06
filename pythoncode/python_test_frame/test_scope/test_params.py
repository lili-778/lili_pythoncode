import pytest


@pytest.fixture(params=[1,2,3])
def data(request):
    return request.param

def test_data(data):
    print(f"测试数据：data {data}")
    assert data<2 , '数据错误'

print(test_data(1))