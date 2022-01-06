

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

class TestRemote():
    def setup(self):
        # 创建一个选项options
        opt=Options()
        # 创建一个远程ip端口9222
        opt.debugger_address="127.0.0.1:9222"
        # 把选项应用到Chrome浏览器中
        self.driver=webdriver.Chrome(options=opt)

    def teardown(self):
        self.driver.quit()

    def test(self):
        # 打开百度首页，选择搜索框，输入111
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("111")
        # self.driver.get_cookie()