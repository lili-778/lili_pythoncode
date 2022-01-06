from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
def ceshiren():
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    def wait_ele_for(driver):
        eles=driver.find_elements(By.XPATH,"//*[@id='kw']")
        driver.close()
        return  len(eles)>0
    # 此处需要先定义函数再触发等待
    WebDriverWait(driver, 10).until(wait_ele_for)

ceshiren()