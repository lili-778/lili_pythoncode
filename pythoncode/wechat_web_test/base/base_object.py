import time

import yaml
from selenium import webdriver


class BasePage:
    _base_url = None
    def __init__(self,base_driver=None):
        # 如果base_driver不为空，则继续执行，不会重复打开新的企业微信页面
        if base_driver:
            self.driver=base_driver
        # 如果base_driver为空则进行第一次实例化，
        else:
            self.driver=webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
            self.driver.implicitly_wait(10)
            # 打开之前登陆后获取的cookies文件,存放在data目录下
            with open("../data/cookies.yml", "r") as f:
                cookies=yaml.safe_load(f)
            # 使用for循环遍历cookie文件，并加载
            for coo_1 in cookies:
                self.driver.add_cookie(coo_1)
            # 打开登陆后的企业微信网址
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

if __name__=="__main__":
    test = BasePage()
