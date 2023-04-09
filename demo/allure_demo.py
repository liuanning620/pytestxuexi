# -*- coding:utf-8 -*-
"""
@author: Alan
@file: allure_demo.py
@time: 2023/3/19 11:34
@desc:  生成html报告：
# allure generate report/result -o report/html --clean
excel中，
allure.feature：sheet名称
allure.story:模块名称
allure.title：用例ID+接口名称
allure.description：请求类型，url，期望结果
"""

import pytest
import allure

#
# 测试方法
@allure.title("用例方法上面allure.title()-----标题：test11111")
@allure.description("测试用例1执行结果是test1")
@allure.severity(allure.severity_level.NORMAL)
def test_1():
    print("------test1------")


@allure.title("用例方法上面allure.title()-----标题：test22222")
@allure.description("测试用例2执行结果是test2")
@allure.severity(allure.severity_level.MINOR)
def test_2():
    print("------test2------")


@allure.feature("class类上面--------allure.feature一级标签---------")
class TestAllure:
    @allure.title("测试用例3--------allure.title标题-----")
    @allure.description("测试用例3-------allure.description描述---------")
    @allure.story("测试用例3-------allure.story二级标签---------")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_3(self):
        print("------test3------")

    @allure.title("测试用例4--------allure.title标题-----")
    @allure.story("测试用例4--------allure.story二级标签------------")
    @allure.description("测试用例4--------allure.description描述------------")
    def test_4(self):
        print("------test4------")

    @pytest.mark.parametrize('case',["case5-1", "case5-2"])
    def test_5(self, case):
        print("------{}------".format(case))
        allure.dynamic.title(case)


if __name__ == '__main__':
    pytest.main(["allure_demo.py"])
