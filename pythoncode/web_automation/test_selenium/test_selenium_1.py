import logging
import time

from selenium import webdriver
from loguru import logger
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_search():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    search=driver.find_element_by_id("su").get_attribute("value")
    # assert  search=="百度"
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.TAG_NAME,"class")))
    driver.close()

# def ceshiren():
#     driver=webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     def wait_ele_for(driver):
#         eles=driver.find_elements(By.XPATH,"//*[id='kw']")
#         driver.close()
#         return  len(eles)>0
#     # 此处需要先定义函数再触发等待
#     WebDriverWait(driver, 10).until(wait_ele_for)


class TestHogwarts():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    # def test_hogwarts(self):
    #     self.driver.get("https://ceshiren.com")
    #     category_name=(By.LINK_TEXT,"测试答疑")
    #     WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(category_name))
    #     self.driver.find_element(*category_name).click()
    # def test_baidu1(self):
    #     self.driver.get("https://www.baidu.com")
    #     self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
    #     self.driver.find_element_by_id("su").click()
    #     # ActionChains(self.driver).double_click(self.driver.find_element_by_id("su")).perform()
    #     time.sleep(5)
    #     self.driver.find_element_by_id("kw").clear()
    #     time.sleep(5)
    def test_baidu2(self):
        self.driver.get("https://www.baidu.com")
        search=self.driver.find_element(By.ID,"su")
        logger.info(search.get_attribute("value"))
        logger.info(search.location)
        logger.info(search.size)
        self.driver.refresh()
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.minimize_window()
        time.sleep(1)
        self.driver.set_window_size(1000,1000)
        time.sleep(1)
    def test_action(self):
        self.driver.get("https://ceshiren.com/")
        action=ActionChains(self.driver)
        search=self.driver.find_element(By.XPATH,"//*[@id='search-button']")
        action.click(search).perform()
        time.sleep(2)

    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        action=ActionChains(self.driver)
        ele_double_c=self.driver.find_element(By.XPATH,"//*[@value='dbl click me']")
        ele_click=self.driver.find_element(By.XPATH,"//*[@value='click me']")
        ele_context_c=self.driver.find_element(By.XPATH,"//*[@value='right click me']")
        ele_clear=self.driver.find_element(By.XPATH,"//*[@value='Clear']")
        ele_cc = self.driver.find_element(By.XPATH, "/html/body/form/textarea")
        action.double_click(ele_double_c)
        action.click(ele_click)
        action.context_click(ele_context_c)
        action.click(ele_clear)
        time.sleep(5)
        action.click(ele_cc)
        time.sleep(2)
        action.send_keys("我们都是好孩子")
        action.perform()
        action.move_by_offset()

    def test_drag_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag1=self.driver.find_element(By.ID,"dragger")
        item1=self.driver.find_element(By.XPATH,"/html/body/div[2]")
        item2 = self.driver.find_element(By.XPATH, "/html/body/div[3]")
        item3 = self.driver.find_element(By.XPATH, "/html/body/div[4]")
        item4 = self.driver.find_element(By.XPATH, "/html/body/div[5]")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag1,item1).wait(2)
        action.drag_and_drop(drag1, item2)
        action.drag_and_drop(drag1, item3)
        action.drag_and_drop(drag1, item4)
        action.perform()
        time.sleep(2)
        self.driver.refresh()

    def test_frame(self):
        self.driver.get("https://sahitest.com/demo/iframesTest.htm")
        # 点击第一个frame的元素
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[1]/a[1]").click()
        # 点击第二个frame的元素
        time.sleep(4)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//*[@id='another']/iframe"))
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[1]/a[1]").click()

        action=ActionChains(self.driver)
        action.move_by_offset(0,1000).perform()
        # 怎么滚动到最下方？？？
        time.sleep(4)
    def test_alert(self):
        self.driver.get("https://sahitest.com/demo/alertTest.htm")
        self.driver.find_element(By.XPATH,"//*[@value='Click For Alert']").click()
        time.sleep(5)
        alert=self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)

    def test_prompt(self):
        self.driver.get("https://sahitest.com/demo/promptTest.htm")
        self.driver.find_element(By.XPATH,"//*[@value='Click For Prompt']").click()
        time.sleep(2)
        prompt=self.driver.switch_to.alert
        prompt.send_keys('我们都是好孩子')
        time.sleep(8)
        prompt.accept()
        # prompt.dismiss()
        time.sleep(2)
        self.driver.refresh()




