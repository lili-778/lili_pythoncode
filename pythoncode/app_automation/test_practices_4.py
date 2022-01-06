from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo3:
    def setup(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="emulator-5554"
        self.desired_cps["appPackage"]="io.appium.android.apis"
        self.desired_cps["appActivity"]=".ApiDemos"
        self.desired_cps["unicodeKeyboard"]=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    def test_toast(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0))').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0))').click()
        sleep(2)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Search']").click()
        # print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
        # self.driver.execute_script()


