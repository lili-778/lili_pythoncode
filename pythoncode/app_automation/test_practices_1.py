'''
打开雪球 app
点击搜索输入框
向搜索输入框输入 “阿里巴巴”
在搜索的结果里选择阿里巴巴，然后点击
获取这只上香港 阿里巴巴的股价，并判断这只股价的价格>200
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo1:
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion']='6.0'
    desired_caps['deviceName'] = '127.0.0.1:7555'
    desired_caps['appPackage'] = 'com.xueqiu.android'
    desired_caps['appActivity'] = '.common.MainActivity'
    def setup(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        # self.desired_caps['platformVersion']='6.0'
        self.desired_caps['deviceName'] = '127.0.0.1:7555'
        self.desired_caps['appPackage'] = 'com.xueqiu.android'
        self.desired_caps['appActivity'] = '.common.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(6)
    def test_xueqiu(self):
        # 点击搜索输入框
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tv_search']").click()
        # 向搜索输入框输入 “阿里巴巴”
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 在搜索的结果里选择阿里巴巴，然后点击
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/ll_stock_item_container']/android.widget.FrameLayout[2]").click()
        # 获取这只香港阿里巴巴的股价，并判断这只股价的价格 < 200
        ele=self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/stock_current_price").get_attribute("text")
        assert float(ele) < 200
    def teardown(self):
        self.driver.quit()