from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo3:
    def setup(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="emulator-5556"
        # self.desired_cps["unicodeKeyboard"]=True
        self.desired_cps["appPackage"]="io.appium.android.apis"
        self.desired_cps["appActivity"]="io.appium.android.apis.ApiDemos"
        self.desired_cps["chromedriverExecutable"]=r"D:\a_lili_all_setup\python\chromedriver.exe"
        self.desired_cps["noReset"]="true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()

    def test_mobile_APIDemo(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0)) ').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0))').click()
        contexts_list=self.driver.contexts
        print(contexts_list)
        self.driver.switch_to.context(contexts_list[-1])
        self.driver.find_element(MobileBy.ID,"i am a link").click()
        sleep(2)
        self.driver.back()
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").clear()
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").send_keys("tongtong")
        sleep(10)