from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        self.desired_cps = {}
        self.desired_cps["platformName"] = "Android"
        self.desired_cps["deviceName"] = "1257.0.0.1:7555"
        # self.desired_cps["unicodeKeyboard"]=True
        self.desired_cps["appPackage"] = "com.tencent.wework"
        self.desired_cps["appActivity"] = ".launch.WwMainActivity"
        # self.desired_cps["chromedriverExecutable"] = r"D:\a_lili_all_setup\python\chromedriver.exe"
        self.desired_cps["noReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(7)
    def teardown(self):
        self.driver.quit()
    def test_wc(self):
        '''
        通讯录添加成员用例步骤
        打开【企业微信】应用
        进入【通讯录】页面
        点击【添加成员】
        点击【手动输入添加】
        输入【姓名】【手机号】并点击【保存】
        验证点：登录成功提示信息
        '''
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1r' and @text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/j_o").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bf_").send_keys("张小美10")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ge4").send_keys("18317154576")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ana").click()
        sleep(2)
        print(self.driver.page_source)
        result=self.driver.find_element(MobileBy.XPATH ,"//*[@class='android.widget.Toast']").get_attribute("text")
        assert  result=="添加成功"



