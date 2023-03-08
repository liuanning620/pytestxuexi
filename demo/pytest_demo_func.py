# -*- coding:utf-8 -*-
"""
@author: Alan
@file: pytest_demo_func.py
@time: 2023/3/8 10:17
@desc: 
"""

import pytest
# 1.创建测试方法
# 2.使用pytest运行

# 定义一个方法，用来测试
def func(x):
    return x+1

# 断言方法,断言成功
def test_a():
    print("test a")
    assert func(3) == 4

# 断言方法,断言失败
def test_b():
    print("test b")
    assert func(3) == 5

if __name__ == '__main__':
    pytest.main(['pytest_demo_func.py'])
