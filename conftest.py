# -*- coding:utf-8 -*-
"""
@author: Alan
@file: conftest.py.py
@time: 2023/3/8 13:57
@desc: 测试用例收集完成时，将收集到的item的name和nodeid的中文显示
"""

#
# def pytest_collection_modify_items(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")