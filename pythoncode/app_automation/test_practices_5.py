from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestDemo3:
    def setup(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="emulator-5556"
        self.desired_cps["appPackage"]="com.xueqiu.android"
        self.desired_cps["appActivity"]=".common.MainActivity"
        self.desired_cps["unicodeKeyboard"]=True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("searchkey,type,price",(['阿里巴巴','BABA',150],['小米','01810',10]))
    def test_param(self,searchkey,type,price):
        pass
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索的结果里选择阿里巴巴，然后点击
        5.获取这只上香港 阿里巴巴的股价，并判断这只股价的价格>200
        6.通过参数化的方法，用一个用例判断阿里巴巴和小米的股价
        :return:
        """
        self.driver.find_element(By.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys(f"{searchkey}")
        self.driver.find_element(By.XPATH,f"//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='{type}']").click()
        current_price=self.driver.find_element(By.ID,"com.xueqiu.android:id/stock_current_price").text
        assert float(current_price) >price
        sleep(5)



