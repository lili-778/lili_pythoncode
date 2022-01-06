import os
from time import sleep

from appium  import webdriver

from app_Automation_2.podemo.base.base_method import Base_Method
from app_Automation_2.podemo.page.main_page import MainPage


class App_Base(Base_Method):

    # 启动微信app
    def app_start(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="127.0.0.1:7555"
        self.desired_cps["appPackage"]="com.tencent.wework"
        self.desired_cps["appActivity"]=".launch.WwMainActivity"
        self.desired_cps["noReset"]="true"
        self.desired_cps["automationName"]="uiautomator2"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(5)
    # 关闭app
    def app_end(self):
        self.driver.quit()

    # 进入微信主程序，返回首页
    def goto_main(self):
        return MainPage(self.driver)

    def reback_main(self):
        os.system("adb shell am force-stop com.tencent.wework")
        os.system("adb shell am start -n com.tencent.wework/.launch.WwMainActivity")
        sleep(5)
        return MainPage(self.driver)