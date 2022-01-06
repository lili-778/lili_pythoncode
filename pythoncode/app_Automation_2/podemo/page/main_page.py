
# 定义首页
from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.addresslist_page import Addresslist_Page


class MainPage(Base_Method):

    def goto_contact(self):
        # 使用封装好的方法点击通讯录，返回通讯录页面
        self.find_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1r' and @text='通讯录']")
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1r' and @text='通讯录']").click()
        return Addresslist_Page(self.driver)
