from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote import webelement


class TestChains:
    def setup(self):
        self.driver=webdriver.Chrome()
    def teardown(self):
        self.driver.quit()

    def test_weixin_sleep(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(30)
        cookies=self.driver.get_cookies()
        with open("../../wechat_web_test/data/cookies.yml", "w") as f:
            yaml.safe_dump(cookies,f)
        print(cookies)
    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        with open("../../wechat_web_test/data/cookies.yml", "r") as f:
            cookies=yaml.safe_load(f)
            print(cookies)
        for coo in cookies:
            self.driver.add_cookie(coo)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(5)

