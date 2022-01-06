from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.editmember_page import Editmember_Page


class Addmember_Page(Base_Method):

    def addmember_manual(self):
        # 添加成员页面点击手动输入添加，跳转到编辑成员页面
        self.find_click(MobileBy.ID, "com.tencent.wework:id/j_o")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/j_o").click()
        return Editmember_Page(self.driver)