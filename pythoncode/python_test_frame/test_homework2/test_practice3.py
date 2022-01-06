import logging

import allure
import pytest
import yaml

from test_homework2.test_calc import Calculator as calc


def get_add_datas(level):
    with open("./datas/data.yml",encoding="utf-8") as  f:
        datas=yaml.safe_load(f)
        data_add=datas["add"]
        return (data_add.get(level).get("datas"),data_add.get(level).get("ids"))

@pytest.fixture(params=get_add_datas("P1_1")[0],ids=get_add_datas("P1_1")[1])
def add_P1_1(request):
    return request.param

@pytest.fixture(params=get_add_datas("P1_2")[0],ids=get_add_datas("P1_2")[1])
def add_P1_2(request):
    return request.param

@pytest.fixture(params=get_add_datas("P0")[0],ids=get_add_datas("P0")[1])
def add_P0(request):
    return request.param

@pytest.fixture(params=get_add_datas("P3")[0],ids=get_add_datas("P3")[1])
def div_P3(request):
    return request.param

@pytest.fixture(params=get_add_datas("P2")[0],ids=get_add_datas("P2")[1])
def add_P2(request):
    return request.param

class TestDemo():
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def test_add_case_p1_1(self, add_P1_1):
        with allure.step("添加第一个数"):
            a = add_P1_1[0]
            print(a)
        with allure.step("添加第二个数"):
            b = add_P1_1[1]
            print(b)
        with allure.step("添加第三个数"):
            expect = add_P1_1[2]
            print(expect)
        with allure.step("汇总数据"):
            print(f"{a}+{b}={expect}")
        assert expect == calc().add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.add
    def test_add_case_p1_2(self,add_P1_2):
        a=add_P1_2[0]
        b = add_P1_2[1]
        expect = add_P1_2[2]
        with pytest.raises(eval(expect)) as e:
            print(f"{a}+{b}={expect}")
            # logging.info(f"输入数据 {a} {b} 期望数据 {expect}")
            result = calc().add(a, b)
        assert expect == e.typename

    @pytest.mark.run(order=3)
    @pytest.mark.add
    def test_add_case_p0(self, add_P0):
        a = add_P0[0]
        b = add_P0[1]
        expect = add_P0[2]
        print(f"{a}+{b}={expect}")
        assert expect == calc().add(a, b)

    @pytest.mark.run(order=5)
    @pytest.mark.add
    def test_add_case_p2(self,add_P2):
        a=add_P2[0]
        b = add_P2[1]
        expect = add_P2[2]
        with pytest.raises(eval(expect)) as e:
            print(f"{a}+{b}={expect}")
            # logging.info(f"输入数据 {a} {b} 期望数据 {expect}")
            result = calc().add(a, b)
        assert expect == e.typename

    @pytest.mark.run(order=4)
    @pytest.mark.div
    def test_div_case_P3(self,div_P3):
        a = div_P3[0]
        b = div_P3[1]
        expect = div_P3[2]
        print(f"{a}+{b}={expect}")
        assert expect == calc().div(a, b)

    def test_attach_picture(self):
        allure.attach.file("./datas/picture.png",name="截图",attachment_type=allure.attachment_type.PNG)
        pass


