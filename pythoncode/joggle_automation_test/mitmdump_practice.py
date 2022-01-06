import json

import mitmproxy.http
from mitmproxy import http, ctx


class AddHeader:
    def __init__(self):
        self.num=0

    # def request(self,flow:http.HTTPFlow):
    #     print('This is a demo!')
    #     if 'quote.json' in flow.request.pretty_url and '_t' in flow.request.pretty_url \
    #                         and 'x=' in flow.request.pretty_url:
    #         with open('D:/quote1.json','r',encoding='utf-8') as  f:
    #             print(flow)
    #             flow.response=http.Response.make(200,f.read(),{'Content-Type':'application/data'})
    #                           # http.HTTPFlow.response.make()
    #             print('=================')
    #             print(flow)
    #             print('=================')
    #             print(http.HTTPFlow.response)
    #             print('=================')
    #             print(flow.response.headers)
    #             print('=================')

    # def response(self,flow:http.HTTPFlow):
    #     if 'quote.json' in flow.request.pretty_url and '_t' in flow.request.pretty_url \
    #             and 'x=' in flow.request.pretty_url:
    #         print('========================')
    #         data_obj=json.loads(flow.response.text)
    #         print(data_obj)
    #         print('========================')
    #         print(flow.request.url)
    #         data_obj['data']['items'][0]['quote']['name']='1 4women都是坏孩子11'
    #         flow.response.text=json.dumps(data_obj)
    def request(self,flow:http.HTTPFlow):
        if 'ceshiren' in flow.request.pretty_url:
            with open('./demo/test.yml','r',encoding='utf-8') as f:
                flow.response=http.Response.make(200,f.read())

addons=[AddHeader()]
# AddHeader()

# num=0
# def response(flow:http.HTTPFlow):
#     global num
#     num=num+1
#     flow.response.headers['count']=str(num)
#     print('this is a demo',num)
#     print(flow.response.headers)