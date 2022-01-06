import logging
from time import sleep

import pytest
import yaml

from app_Automation_2.podemo.base.app_base import App_Base
from app_Automation_2.podemo.base.generate_data import Generate_Data


class Test_Contact():
    data = Generate_Data.gene_name_phone(2)
    def setup_class(self):
        self.app = App_Base()
        # 启动企业微信
        self.app.app_start()
        # 进入企业微信首页
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.app_end()

    def setup(self):
        pass

    def teardown(self):
        sleep(4)
        self.app.reback_main()

    # 测试企业微信添加联系人功能,每次都自动生成两条数据并执行两遍
    @pytest.mark.parametrize("name,phone",data)
    def test_addcontact(self,name,phone):
        # 将日志输出到文件mylog.log,并打印到控制台
        self.main.get_logger().info(f"添加的联系人是{name}，手机号码是{phone}")
        result=self.main.goto_contact().add_member().addmember_manual().edit_member(name,phone)
        # 添加断言
        assert result == "添加成功"
    # 测试企业微信删除联系人
    def test_deletecontact(self):
        name="李"
        # 将日志输出到文件mylog.log,并打印到控制台
        self.main.get_logger().info(f"删除的联系人是{name}")
        # search_member方法返回两个值,search_member()返回一个元组并赋值给一个对象
        self.search_page=self.main.goto_contact().search_member(name)
        # 在删除成员操作之前，先获取搜索页面成员数量并进行判断，如果为0，则打印出没有搜索结果
        amount=self.search_page[1]
        if amount==0:
            print("无搜索结果")
        else:
            # 此处有搜索结果前提下
            # 删除成员操作之后，获取搜索页面成员数量
            amount_d=self.search_page[0].individual_info_1().individual_info_2().editmember_info()
            # 将amount_d与search_mamber方法里的amount-1进行比较，相等则删除成功，否则删除失败
            # print(amount,amount_d)
            if amount_d == amount - 1:
                print("删除成功！")
            else:
                print("删除失败！")
