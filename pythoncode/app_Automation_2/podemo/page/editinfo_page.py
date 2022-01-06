from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app_Automation_2.podemo.base.base_method import Base_Method


class Edit_Info(Base_Method):

    def editmember_info(self):
        #页面滑动到最下方点击删除成员
        self.scroll_find_id_click("com.tencent.wework:id/f7w")
        # self.driver.find_element_by_android_uiautomator\
        #     ('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.tencent.wework:id/f7w").instance(0))').click()
        # 弹出框点击确定
        self.find_click(MobileBy.ID, "com.tencent.wework:id/c10")
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c10").click()
        # 返回搜索页面，重新计算页面的重复姓名人数，人数-1说明删除成功，否则删除失败
        sleep(4)
        # 重新计数之前，需要等待几秒刷新页面
        member_list_d = self.finds(MobileBy.ID, "com.tencent.wework:id/bgr")
        # member_list_d = self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/bgr")
        amount_d = 0
        for i in member_list_d:
            # 获取删除后重复姓名的人数
            amount_d += 1
        return  amount_d