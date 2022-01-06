from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method


class Editmember_Page(Base_Method):
    def edit_member(self,name,phone):
        # 编辑成员页面，输入姓名和手机号，点击保存
        # 使用封装方法定位元素
        # 输入姓名
        self.find(MobileBy.ID, "com.tencent.wework:id/bf_").send_keys(name)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bf_").send_keys(name)
        # 输入手机号
        self.find(MobileBy.ID, "com.tencent.wework:id/ge4").send_keys(phone)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ge4").send_keys(phone)
        # 点击保存
        self.find_click(MobileBy.ID, "com.tencent.wework:id/ana")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ana").click()
        # 获取toast弹窗所对应的文本元素
        result=self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        # result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        sleep(5)
        # 将result返回
        return result