import sys
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
        self.desired_cps["appPackage"]="com.xueqiu.android"
        self.desired_cps["appActivity"]=".view.WelcomeActivityAlias"
        self.desired_cps["chromedriverExecutable"]=r"D:\a_lili_all_setup\python\chromedriver.exe"
        self.desired_cps["noReset"]="true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()

    def test_mobile_baidu(self):
        '''
        点击交易
        点击 A 股开户
        输入用户名和密码
        点击立即开户
        退出应用
        注：打开新的页面其实就是一个新的窗口了，要切换窗口句柄了
        '''
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/tabs']/android.widget.RelativeLayout[3]").click()
        contexts_list=self.driver.contexts
        print('第一次获取上下文',contexts_list)
        self.driver.switch_to.context(contexts_list[-1])
        self.driver.find_element(By.CSS_SELECTOR,"#app>div>div>div>ul>li.trade_home_danjuan_23L>div.trade_home_info_205>h1").click()
        # window_list=self.driver.window_handles
        # print(window_list)
        # self.driver.switch_to.window(window_list[-1])
        self.driver.switch_to.context(contexts_list[0])
        contexts_list = self.driver.contexts
        print('第二次获取上下文',contexts_list)
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/btn_login']").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/et_telephone").send_keys("18317185640")
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/et_password").send_keys("111111")
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/vg_login_btn").click()
        assert  self.driver.find_element(MobileBy.XPATH,"//*[@text='验证码已过期']").is_enabled()
        # print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/content']/android.widget.FrameLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        sleep(5)
        sys.exc_info()

def student_grade(grade):
    def output_students(name,gender):
        print(f"学院开学啦！姓名{name}，性别是{gender}，年级是{grade}")
    return output_students

# ele=student_grade(5)
# ele('lili',"女")

