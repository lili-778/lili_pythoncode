import pytest
import yaml

from wechat_web_test.page_object.main_page import MainPage

class TestAddMember:
    mem_name, mem_account, mem_phone = '钱25','125','18811112235'
    def setup(self):
        self.main=MainPage()
    def test_add_member(self):
        # 调用类里的方法

        res= self.main.goto_add_mem().add_member(self.mem_name,self.mem_account,self.mem_phone).get_list()
        assert  self.mem_name in res

    def test_add_member_fail(self):
        # 调用类里的方法
        res= self.main.goto_add_mem().add_member_name_fail()
        print(res)

    def teardown(self):
        print("测试结束！")
        self.main.driver.quit()
