# -*- coding:utf-8 -*-
"""
@author: Alan
@file: Test_demo.py
@time: 2023/3/8 9:56
@desc: 
"""
import pytest
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
from common.Base import init_db

# {'code': 201, 'msg': {'userId': 1, 'title3': '标题', 'body': 'this is a writer 3', 'id': 101}}


def test_add_id():
    url = "http://jsonplaceholder.typicode.com/posts"
    data = {
        "userId": 3,
        "title": "title3",
        "body": "this is a writer 3"
    }
    req = Request()
    res = req.post(url=url,json=data)
    code = res["code"]
    AssertUtil().assert_code(code, 201)
    body = res["msg"]
    expected_body = "this is a writer 3"
    content = body["body"]
    AssertUtil().assert_in_body(body,expected_body)
    conn =init_db("db_1")
    res = conn.fetchone("select content from title where userId = 3")
    assert content == res["content"]
test_add_id()
# if __name__ ==  "__main__":
#     pytest.main["-s"]