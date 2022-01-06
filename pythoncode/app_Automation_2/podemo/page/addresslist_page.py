from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.addmember_page import Addmember_Page
from app_Automation_2.podemo.page.memberinfo_page_1 import Member_Info_1


class Addresslist_Page(Base_Method):
    def add_member(self):
        # 点击添加成员，返回到添加成员页面
        text = "添加成员"
        self.scroll_find_text_click(text)
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        return Addmember_Page(self.driver)
    def search_member(self,name):
        # 点击搜索,进入搜索输入框页面
        self.find_click(MobileBy.ID, "com.tencent.wework:id/j08")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/j08").click()
        # 输入重复的姓名进行搜索
        self.find(MobileBy.ID, "com.tencent.wework:id/hj9").send_keys(name)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hj9").send_keys("小小")
        # 定位具有重复姓名的人的页面元素
        member_list = self.finds(MobileBy.ID, "com.tencent.wework:id/bgr")
        # member_list = self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/bgr")
        amount = 0
        for i in member_list:
            # 获取当前重复姓名的人数
            amount += 1
        # print(amount)
        # 判断有无搜索结果，并进行相应的处理
        if amount==0:
            return Member_Info_1(self.driver),amount
        else:
            # 点击第一个重复姓名,进入个人信息页面
            self.find_click(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/hkj']/android.widget.RelativeLayout[2]")
            # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/hkj']/android.widget.RelativeLayout[2]").click()
            return Member_Info_1(self.driver),amount
