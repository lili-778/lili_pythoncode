'''
打开雪球首页
定位首页的搜索框
判断搜索框是否可用，并查看搜索框 name 属性值
打印搜索框这个元素的左上角坐标和它的宽高
向搜索框输入：alibaba
判断阿里巴巴是否可见
如果可见，打印搜索成功点击，如果不可见，打印搜索失败
'''
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDemo2:
    def setup(self):
        self.desired_cps={}
        self.desired_cps["platformName"]="Android"
        self.desired_cps["deviceName"]="127.0.0.1:7555"
        self.desired_cps["appPackage"]="com.xueqiu.android"
        self.desired_cps["appActivity"]=".common.MainActivity"
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.desired_cps)
        self.driver.implicitly_wait(6)
    def test_xueqiu2(self):
        # 定位首页的搜索框
        search=self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_search']")
        # 判断搜索框是否可用，并查看搜索框name属性值
        print(f"判断搜索框是否可用:{search.is_enabled()}")
        print(f"搜索框name属性值:{search.get_attribute('text')}")
        # 打印搜索框这个元素的左上角坐标和它的宽高
        print(f"搜索框左上角坐标:{search.location},宽高:{search.size}")
        # 点击搜索输入框
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_search']").click()
        # 向搜索框输入：alibaba
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 判断阿里巴巴是否可见
        ele=self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
        if ele.is_displayed():
            print(ele.is_displayed())
            print("搜索成功")
        # 如果可见，打印搜索成功点击，如果不可见，打印搜索失败
    def test_xueqiu_scroll(self):
        '''
        进入雪球应用
        再主页从下往上滑动
        避免使用坐标（代码用获取屏幕的长宽来解决这个问题）
        '''
        # 定义一个touchaction对象
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/title_text' and @text='热门']").click()
        time.sleep(5)
        windows=self.driver.get_window_rect()
        win_width=windows["width"]
        win_height=windows["height"]
        print(win_width,win_height)
        x1=int(win_width/2)
        # print(type(x1))
        y1=int(win_height*1/5)
        y2=int(win_height*4/5)
        action=TouchAction(self.driver)
        e1 =  self.driver.find_element(MobileBy.XPATH,"//*[@text='我的']")
        # e2 =  self.driver.find_element(MobileBy.XPATH,"//*[@text='申请专栏']")
        action.press(x=x1, y=y1).wait(2000).move_to(x=x1, y=y2).wait(2000).release().perform()
        # action.press(x=x1, y=y2).wait(2000).move_to(x=x1, y=y1).wait(2000).release().perform()
        time.sleep(5)

    def teardown(self):
        self.driver.quit()
