from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.memberinfo_page_2 import Member_Info_2


class Member_Info_1(Base_Method):
    def individual_info_1(self):
        #点击右上角三个点
        self.find_click(MobileBy.ID,"com.tencent.wework:id/izx")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/izx").click()
        # 返回到个人信息编辑页面
        return  Member_Info_2(self.driver)