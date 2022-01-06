from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestDemo:
    def setup(self):
        self.desired_cps = {}
        self.desired_cps["platformName"] = "Android"
        self.desired_cps["deviceName"] = "127.0.0.1:7555"
        # 微信包名和活动名
        self.desired_cps["appPackage"] = "com.tencent.mm"
        self.desired_cps["appActivity"] = ".ui.LauncherUI"
        self.desired_cps["chromeOptions"]= {"androidProcess":"com.tencent.mm"}
        # 不清除app的缓存数据
        self.desired_cps["noReset"] = "true"
        # 跳过设备初始化
        self.desired_cps["skipDeviceInitialization"] = "true"
        # 跳过服务的安装
        self.desired_cps["skipServerInstallization"] = "true"
        # 在页面动态加载时，等待空闲超时时间默认是10秒
        # self.desired_cps["setting[waitForIdleTimeout]"]=0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_proce(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.mm:id/e8y']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]").click()
        size=self.driver.get_window_size()
        print(size)
        height=size["height"]
        width=size["width"]
        start_x=width/2
        start_y=height/5
        end_y=height*4/5
        self.driver.swipe(start_x,start_y,start_x,end_y)
        # 点击雪球小程序
        self.driver.find_element(MobileBy.XPATH,"//*[@text='雪球']").click()
        sleep(20)
        print(self.driver.contexts)
        # 输入股票信息
        self.driver.find_element(MobileBy.XPATH,"//*[@content-desc='搜索股票信息/代码']").click()


