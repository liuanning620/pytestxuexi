# -*- coding:utf-8 -*-
"""
@author: Alan
@file: pytest_demo_class.py
@time: 2023/3/8 10:34
@desc: 
"""
import pytest


# 创建测试方法，test开头
# 创建setup_class方法，teardown_class方法------每个类中只执行一次
# 创建setup方法，teardown方法------每个方法都执行一次

# 失败重跑----失败重试2次，失败重试等待时间1s
# @pytest.mark.flaky(reruns=2, reruns_delay=1)

# 参数化：argnames：参数名；argvalues：参数对应值，必须可迭代，单个参数一般是list
# @pytest.mark.parametrize(argnames,argvalues)
# 例如单个参数
# data_list_one = ["张三", "李四"]
# @pytest.mark.parametrize(name,data_list_one)

# 多个参数一般list中每个元素都是元组，元组中的元素与参数一一对应
# @pytest.mark.parametrize(argname1,argname2,argvalues)
# 例如多个参数
# data_list_all = [("张三", "男性"), ("李四", "女性")]
# @pytest.mark.parametrize(("name","sex"),data_list_all)

# 不指定运行目录和文件时，pytest会执行当前目录下所有test开头和_test结尾的文件中的test开头的函数


class TestFunc:

    # 创建setup_class方法，teardown_class方法,每个类中只执行一次
    def setup_class(self):
        print("---------test setup_class-----------")

    def teardown_class(self):
        print("-----------test teardown_class------------")

    # 创建setup方法，teardown方法,每个方法都执行一次
    def setup(self):
        print("---------test setup-----------")

    def teardown(self):
        print("-----------test teardown------------")

    # 定义两个测试方法
    def test_a(self):
        print("------test a---------")
        assert 3 == 3

    def test_b(self):
        print("-----test b-------")
        assert 3 == 4

    # 当前用例失败重试2次，失败重试等待时间1s，而配置文件是3次，2秒，其他用例执行配置文件的条件
    @pytest.mark.flaky(reruns=2,reruns_delay=1)
    def test_c(self):
        print("-----test c-------")
        assert 4 == 5

class TestParametrize:
    # 定义参数化数据,一个参数
    data_list_one = ["张三", "李四"]

    @pytest.mark.parametrize("name",data_list_one)
    def test_d(self,name):
        print("-----test d-----")
        print(name)
        assert 1==1

    # 定义参数化数据,一多个参数，用元祖和列表
    data_list_all = [("张三", "男性"),("李四", "女性")]

    @pytest.mark.parametrize(("name","sex"),data_list_all)
    def test_f(self,name,sex):
        print("-----test f-----")
        print(name,sex)
        assert 1==1

class TestName:
    # 定义参数化数据,一个参数
    data_list_one = ["张三", "李四"]

    @pytest.mark.parametrize("name",data_list_one)
    def test_d(self,name):
        print("-----test d-----")
        print(name)
        assert 1==1

    # 定义参数化数据,一多个参数，用元祖和列表
    data_list_all = [("张三", "男性"),("李四", "女性")]

    @pytest.mark.parametrize(("name","sex"),data_list_all)
    def test_f(self,name,sex):
        print("-----test f-----")
        print(name,sex)
        assert 1==1

if __name__ == '__main__':

    # pytest.main(["-s", "pytest_demo_class.py::TestFunc"])
    # [配置文件中加入-s，此处就不用-s了]
    pytest.main(["pytest_demo_class.py::TestFunc"])