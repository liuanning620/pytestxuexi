# -*- coding:utf-8 -*-
"""
@author: Alan
@file: RequestsUtil.py
@time: 2023/3/7 10:18
@desc: 封装requests方法
"""

import requests
from utils.LogUtil import my_log

class Request:
    # 初始化日志
    def __init__(self):
        self.log = my_log("RequestLog")
    # 定义方法
    def request_api(self, url, data=None, json=None, headers=None,cookies=None, method='get'):
        global r
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url=url, data=data, json=json, cookies=None, headers=headers)
        elif method == "post":
            self.log.debug("发送get请求")
            r = requests.post(url=url, data=data, json=json, cookies=None, headers=headers)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text

        res ={}
        res["code"] = code
        res["msg"] = body
        return res

    # 重构get方法
    def get(self,url,**kwargs):
        r = self.request_api(url=url,method="get",**kwargs)
        return r

    def post(self,url,**kwargs):
        r = self.request_api(url=url,method="post",**kwargs)
        return r










