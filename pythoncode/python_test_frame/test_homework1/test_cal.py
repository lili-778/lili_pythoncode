import pytest
import yaml


def add(a,b):
    return a+b
def div(a,b):
    return a/b
def get_add_datas(level):
    with open("./datas/data.yml",encoding="utf-8") as  f:
        datas=yaml.safe_load(f)
        data_add=datas["add"]
        return (data_add.get(level).get("datas"),data_add.get(level).get("ids"))


class TestDemo():
    # def setup_class(self):
    #     pass
    TD_data_add,TD_data_ids1=get_add_datas("P0")
    TD_data_div, TD_data_ids2 = get_add_datas("P1")
    def teardown_class(self):
        print("结束测试")
    def setup(self):
        print("开始计算")
    def teardown(self):
        print("计算结束")
    @pytest.mark.parametrize("a,b,expect",TD_data_add,ids=TD_data_ids1)
    def test_add_case(self,a,b,expect):
        print(f"{a}+{b}={expect}")
        assert expect==add(a,b)

    @pytest.mark.parametrize("a,b,expect",TD_data_div,ids=TD_data_ids2)
    def test_div_case(self,a,b,expect):
        with pytest.raises(eval(expect)) as e:
            result=div(a,b)
        assert expect==e.typename