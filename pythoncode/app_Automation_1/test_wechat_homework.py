from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestDemo:
    def setup(self):
        self.desired_cps = {}
        self.desired_cps["platformName"] = "Android"
        self.desired_cps["deviceName"] = "127.0.0.1:7555"
        self.desired_cps["appPackage"] = "com.tencent.wework"
        self.desired_cps["appActivity"] = ".launch.WwMainActivity"
        # 不清除app的缓存数据
        self.desired_cps["noReset"] = "true"
        # 跳过设备初始化
        self.desired_cps["skipDeviceInitialization"] = "true"
        # 跳过服务的安装
        self.desired_cps["skipServerInstallization"] = "true"
        # 在页面动态加载时，等待空闲超时时间默认是10秒
        self.desired_cps["setting[waitForIdleTimeout]"]=0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_add_member(self):
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
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bf_").send_keys("张小美13")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ge4").send_keys("18317154579")
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ana").click()
        sleep(2)
        print(self.driver.page_source)
        result=self.driver.find_element(MobileBy.XPATH ,"//*[@class='android.widget.Toast']").get_attribute("text")
        assert  result=="添加成功"
    def test_daka(self):
        '''
       实现打卡功能
        打开【企业微信】应用
        进入【工作台】页面
        点击【打卡】
        选择【外出打卡】tab
        点击【第 N 次打卡】
        验证点：提示【外出打卡成功】
        '''
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1r' and @text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.tencent.wework:id/fru").text("打卡").instance(0))').click()
        # 点击立即打卡
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/d3i").click()
        # 点击外出打卡，此处resource-id= com.tencent.wework:id/iir
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 点击第N次打卡
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b4e").click()
        # 或者使用self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        result=self.driver.find_element(MobileBy.ID ,"com.tencent.wework:id/p7").get_attribute("text")
        assert  result=="外出打卡成功"

    def test_delete_member(self):
        '''
        删除成员
        '''
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/f1r' and @text='通讯录']").click()
        # 点击搜索
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/j08").click()
        # 输入重复的姓名进行搜索
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hj9").send_keys("翻")
        # 定位具有重复姓名的人的页面元素
        member_list=self.driver.find_elements(MobileBy.ID,"com.tencent.wework:id/bgr")
        amount=0
        for i in member_list:
            # 获取当前重复姓名的人数
            amount+=1
        # print(amount)
        if amount == 0:
            print("无搜索结果")
        else:
            # 点击第一个重复姓名,进入个人信息页面
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/hkj']/android.widget.RelativeLayout[2]").click()
            # 点击右上角三个点
            self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/izx").click()
            # 点击编辑成员
            self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/bna").click()
            # 页面滑动到最下方点击删除成员
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.tencent.wework:id/f7w").instance(0))').click()
            # 弹出框点击确定
            self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/c10").click()
            # 返回搜索页面，重新计算页面的重复姓名人数，人数-1说明删除成功，否则删除失败
            member_list_d=self.driver.find_elements(MobileBy.ID,"com.tencent.wework:id/bgr")
            amount_d = 0
            for i in member_list:
                # 获取删除后重复姓名的人数
                amount_d += 1
            if amount_d==amount-1:
                print("删除成功！")
            else:
                print("删除失败！")

