from selenium.webdriver.common.by import By

from wechat_web_test.base.base_object import BasePage

class ContactPage(BasePage):
    #通讯录页面有添加成员功能，返回添加成员页面
    def goto_add_member(self):
        #涉及循环导包，需要局部引入
        from wechat_web_test.page_object.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
    def get_list(self):
        mem_list=self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list=[ele.get_attribute("title") for ele in mem_list]
        return  name_list
