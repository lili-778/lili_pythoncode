from selenium.webdriver.common.by import By

from wechat_web_test.base.base_object import BasePage
from wechat_web_test.page_object.add_member_page import AddMemberPage
from wechat_web_test.page_object.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    #首页跳转到通讯录的方法
    def goto_contact(self):
        #返回到通讯录页面
        return ContactPage(self.driver)

    # 首页跳转到添加成员的方法
    def goto_add_mem(self):
        #返回到添加成员页面
        self.driver.find_element(By.XPATH,"//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return AddMemberPage(self.driver)