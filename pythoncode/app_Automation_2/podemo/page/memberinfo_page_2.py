from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.editinfo_page import Edit_Info


class Member_Info_2(Base_Method):
    def individual_info_2(self):
        #点击编辑成员
        self.find_click(MobileBy.ID, "com.tencent.wework:id/bna")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bna").click()
        # 返回到编辑成员页面
        return  Edit_Info(self.driver)