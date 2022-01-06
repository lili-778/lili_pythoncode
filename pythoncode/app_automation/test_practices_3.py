from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo3:
    def setup(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="emulator-5554"
        self.desired_cps["appPackage"]="com.xueqiu.android"
        self.desired_cps["appActivity"]=".common.MainActivity"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        '''
        1.打开雪球app
        2.点击我的，进入到个人信息页面
        3.点击登录，进入到登录页面
        4.输入用户名，输入密码
        5.点击登录
        6.弹出手机号输入失败的提示，并assert这个提示对不对
        '''
        # locator=(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='我的']")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))

        WebDriverWait(self.driver,10).until(lambda x:self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='我的']")).click()

        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/rl_login").childSelector(text("帐号密码登录"))').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456789")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("111111111")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        ele=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/md_content")')
        assert ele.is_displayed()
        sleep(5)

    def test_scroll(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("热门")').click()
        sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("知行合一").instance(0))').click()
        sleep(5)
