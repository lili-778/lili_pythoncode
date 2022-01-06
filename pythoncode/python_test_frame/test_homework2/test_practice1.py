import logging
import pytest
import yaml

from test_homework2.test_calc import Calculator as calc


def get_add_datas(level):
    with open("./datas/data.yml",encoding="utf-8") as  f:
        datas=yaml.safe_load(f)
        data_add=datas["add"]
        return (data_add.get(level).get("datas"),data_add.get(level).get("ids"))


class TestDemo():

    TD_data_add,TD_data_ids1=get_add_datas("P0")
    TD_data_div, TD_data_ids2 = get_add_datas("P2")

    @pytest.mark.parametrize("a,b,expect",TD_data_add,ids=TD_data_ids1)
    def test_add_case_p0(self,a,b,expect):
        print(f"{a}+{b}={expect}")
        logging.info(f"输入数据 {a} {b} 期望数据 {expect}")
        assert expect==calc().add(a,b)

    @pytest.mark.parametrize("a,b,expect",TD_data_div,ids=TD_data_ids2)
    def test_div_case_P2(self,a,b,expect):
        with pytest.raises(eval(expect)) as e:
            print(f"{a}+{b}={expect}")
            logging.info(f"输入数据 {a} {b} 期望数据 {expect}")
            result=calc().div(a,b)
        assert expect==e.typename