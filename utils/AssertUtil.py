# -*- coding:utf-8 -*-
"""
@author: Alan
@file: AssertUtil.py
@time: 2023/3/8 13:14
@desc: 封装断言
"""
import json

from utils.LogUtil import my_log

# 定义封装类
# 初始化数据，日志
# code相等，body相等，body包含

class AssertUtil:
    # 初始化日志
    def __init__(self):
        self.log = my_log("AssertUitl")

    # code是否相同
    def assert_code(self,code,expected_code):
        try:
            assert int(code) == int(expected_code)
            self.log.error("status_code verification passed")
            return True
        except:
            self.log.error("code verification failed,code is: %s, expected_code is: %s"%(code,expected_code))
            raise

    # code是否相同
    def assert_body(self,body,expected_body):
        try:
            assert str(body) == str(expected_body)
            self.log.error("body verification passed")
            return True
        except:
            self.log.error("error: body verification failed , body is: %s, expected_body is: %s"%(body,expected_body))
            raise

    # body是否包含期望
    def assert_in_body(self,body,expected_body):

        try:
            # body = json.dumps(body)
            assert expected_body in body
            self.log.error("in body verification passed")
            return True
        except:
            self.log.error("error: expected_body not in body, body is: %s, expected_body is: %s"%(body,expected_body))
            raise