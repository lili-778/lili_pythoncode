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
        self.desired_cps["unicodeKeyboard"]=True
        self.desired_cps["browserName"]="Chrome"
        self.desired_cps["chromedriverExecutable"]=r"D:\a_lili_all_setup\python\chromedriver.exe"
        self.desired_cps["noReset"]="true"
        self.desired_cps["dontStopAppOnReset"] = "true"
        # self.desired_cps["autoGrantPermissions"]=True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()
    # @pytest.mark.parametrize("searchkey,type,price",(['阿里巴巴','BABA',150],['小米','01810',10]))
    def test_mobile_baidu(self):
        self.driver.get("https://m.baidu.com")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"index-kw")))

        self.driver.find_element(By.ID,"index-kw").send_keys("tongtong")
        self.driver.find_element(By.ID,"index-bn").click()
        sleep(10)



