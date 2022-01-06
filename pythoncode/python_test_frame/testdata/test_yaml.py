import pytest
import yaml


@pytest.mark.parametrize("a,b",yaml.safe_load(open("data.yml")))
def test_foo(a,b):
    print(f"a+b={a+b}")