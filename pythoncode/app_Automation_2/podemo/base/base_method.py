import logging

from appium.webdriver.webdriver import WebDriver
from faker import Faker


class Base_Method:
    def __init__(self,driver:WebDriver= None):
        self.driver = driver
    @classmethod
    def get_name(self):
        return Faker("zh_CN").name()
    @classmethod
    def get_phone(self):
        return Faker("zh_CN").phone_number()

    # 封装反法，后面直接调用,by为定位方式，locator为定位表达式
    def find(self,by,locator):
        # 查找元素
        return self.driver.find_element(by,locator)
    def finds(self,by,locator):
        # 查找元素
        return self.driver.find_elements(by,locator)
    def find_click(self,by,locator):
        # 查找并点击元素
        return self.driver.find_element(by,locator).click()
    def scroll_find_text_click(self,text):
        # 滚动页面查找text文本元素并点击
        self.driver.find_element_by_android_uiautomator\
            (f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0))').click()

    def scroll_find_id_click(self,id):
        # 滚动页面查找id元素并点击
        self.driver.find_element_by_android_uiautomator\
            (f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("{id}").instance(0))').click()

    # 该日志记录器既输出到文件也可以打印到控制台
    def get_logger(self):
        # 创建日志记录器名称并设置级别
        logger = logging.getLogger("simple_logger")
        logger.setLevel(logging.DEBUG)

        # 设置文件处理器并设置级别
        ch1 = logging.FileHandler(filename="../mylog.log", encoding="utf-8")
        ch1.setLevel(logging.DEBUG)

        # 设置流处理器并设置级别
        ch2 = logging.StreamHandler()
        ch2.setLevel(logging.DEBUG)

        # 设置格式器
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        # 将格式器添加到文件处理器中
        ch1.setFormatter(formatter)
        # 将格式器添加到流处理器中
        ch2.setFormatter(formatter)

        # 将文件处理器添加到记录器中
        logger.addHandler(ch1)
        # 将流处理器添加到记录器中
        logger.addHandler(ch2)
        return logger

if __name__=="__main__":
    print(Base_Method.get_name())
    print(Base_Method.get_phone())
    Base_Method().get_logger().info("这个是日志打印!")