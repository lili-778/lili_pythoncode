import time

from selenium.webdriver.common.by import By

from wechat_web_test.base.base_object import BasePage
from wechat_web_test.page_object.contact_page import ContactPage


class AddMemberPage(BasePage):
    #添加成员页面点击通讯录返回通讯录列表页
    def goto_contact(self):
        return ContactPage(self.driver)

    # 添加成员信息保存后，跳转到通讯录页面
    def add_member(self,mem_name,mem_account,mem_phone):
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys(mem_name)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(mem_account)
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(mem_phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_name_fail(self):
        # 添加成员时未输入姓名报错
        # 姓名处输入为空格
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("")
        # 获取姓名处的出错信息并返回
        error=self.driver.find_element(By.XPATH, "//*[@id='username']/../div").text
        return error