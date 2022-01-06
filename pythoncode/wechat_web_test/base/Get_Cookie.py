import time
import yaml
from selenium import webdriver

def test_weixin_cookie():
    driver=webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
    time.sleep(30)
    cookies = driver.get_cookies()
    with open("../data/cookies.yml", "w") as f:
        yaml.safe_dump(cookies, f)
    print(cookies)

if __name__=="__main__":
    test_weixin_cookie()