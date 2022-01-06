import base64
import json

import requests
import yaml
from requests.auth import HTTPBasicAuth


class TestDemo:
    # def test_get(self):
    #     r=requests.get("https://httpbin.testing-studio.com/get")
    #     print(r.status_code)
    #     print(r.text)
    #     print(r.json())
    #
    # def test_query(self):
    #     payload={"level":1,
    #              "name":"dsadsdsd"}
    #     r=requests.get('https://httpbin.testing-studio.com/get',params=payload)
    #     print(r.text)
    #     print(r.headers)
    #
    # def test_post_form(self):
    #     payload = {"level": 1,
    #                "name": "dsadsdsd"}
    #     r=requests.post('https://httpbin.testing-studio.com/post',data=payload,headers={"h":"qw"})
    #     print(r.text)
    #     print(r.json())
    #     # print(r.content)
    #     # print(r.raw)
    #     # print(r.request)
    #     print(r.headers)
    #
    # def test_post_json(self):
    #     payload = {"level": 1,
    #                "name": "dsadsdsd"}
    #     r=requests.post('https://httpbin.testing-studio.com/post',json=payload)
    #     print(r.text)
    #     print(r.json()['json']['level'])
    #     print(r)
    #
    # def test_cookies(self):
    #     header={'User-Agent': 'hogwarts',"Cookie1":"working=1"}
    #     cookie_data={"hogwarts":"school","teacher":"AD"}
    #     # r=requests.get('https://httpbin.testing-studio.com/cookies',headers=header)
    #     r = requests.get('https://httpbin.testing-studio.com/cookies', headers=header, cookies=cookie_data)
    #     # 响应体body
    #     # print(r.text)
    #     # 请求头信息
    #     print(r.request.headers)
    #     # 响应头信息
    #     print(r.headers)

    # def test_form(self):
    #     proxy={"http":"127.0.0.1:8888","https":"127.0.0.1:8888"}
    #     dd={"hogwartys":"12"}
    #     r=requests.post("https://httpbin.testing-studio.com/post",json=dd,proxies=proxy,verify=False)
    #     print(r.text)
    #     print(r.headers)

    def test_timeout_one(self):
        r = requests.get("https://vip.ceshiren.com/#/layout/section")
        print(r.text)
        print(r.content)
    def test_timeout_two(self):
        proxy = {"http": "127.0.0.1:8888", "https": "127.0.0.1:8888"}
        r = requests.post("https://httpbin.testing-studio.com/post", proxies=proxy,verify=False,timeout=3)
    def test_timeout_three(self):
        r = requests.post("https://httpbin.testing-studio.com/post")

    def test_files(self):
        proxy={"http":"127.0.0.1:8888","https":"127.0.0.1:8888"}
        r=requests.post("https://httpbin.testing-studio.com/post",
                        files={'hogwarts_files':("aaaa.txt",open('./11.txt','rb'))},proxies=proxy,verify=False)
        print(r.json())

    def test_auth(self):
        r = requests.post("https://httpbin.testing-studio.com/basic-auth/apple/123",
                          auth=HTTPBasicAuth("apple","123"))
        print(r.text)
        print(r.content)

    def test_encode(self):
        # 生成一个本地服务
        url="http://127.0.0.1:9999/demo.txt"
        r=requests.get(url=url)
        # print(r.content)
        # print(r.text)
        oo=base64.b64decode(r.content)
        print(json.loads(oo))
'''
env={
    "default":"test",
    "testing-studio":{
        "dev":"127.0.0.1",
        "test":"127.0.0.2"
    }
}
env1=[
    (1,2,3),
    (4,5,6),
    {
        "dev": "127.0.0.1",
        "test": "127.0.0.2"
    }
]
with open('./demo/test.yaml','w') as f:
    yaml.safe_dump(env1,f)
    print(11)
'''


# 获取企业微信的access_token两个方法
def test_get_token_1():
    Secret="i7Dh9WoZeyPmMrtl5VKktsYhWK7rOLA65t_OsAdVl9w"
    Corpid="wwda344de601a23b0d"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={Corpid}&corpsecret={Secret}"
    r=requests.get(url=url)
    # print(r.text)
    # print(r.content)
    print(r.json()["access_token"])
def test_get_token_2():
    corpsecret="i7Dh9WoZeyPmMrtl5VKktsYhWK7rOLA65t_OsAdVl9w"
    corpid="wwda344de601a23b0d"
    param={
        "corpsecret":"i7Dh9WoZeyPmMrtl5VKktsYhWK7rOLA65t_OsAdVl9w",
        "corpid":"wwda344de601a23b0d"
    }
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r=requests.get(url=url,params=param)
    print(r.url)

    print(r.json()["access_token"])






