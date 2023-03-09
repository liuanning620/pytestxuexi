# -*- coding:utf-8 -*-
"""
@author: Alan
@file: test_excel_case.py
@time: 2023/3/9 15:12
@desc: 
"""
# 初始化信息
#     初始化测试用例文件、sheet名称
#     获取运行测试用例列表
#     日志
# 测试用例方法，参数化
import json
import os
from time import sleep

import pytest
from config.Conf import ConfigYaml, get_data_path
from common.ExcelData import CaseExcelRunData
from utils.LogUtil import my_log
from common import ExcelConf
from utils.RequestsUtil import Request

# 获取excel文件
case_excel_file = os.path.join(get_data_path(), ConfigYaml().get_conf_excel_file())
# 获取sheet名称
case_sheet_name = ConfigYaml().get_conf_excel_sheet()
# 实例化一次数据，共多次调用
case_run_data = CaseExcelRunData(case_excel_file, case_sheet_name)
# 获取全部数据
case_run_list = case_run_data.get_excel_run_data()
# 日志
log = my_log()


# 执行用例
# 1.增加pytest，修改方法参数，重构函数内容，pytest.main运行
class TestExcelCase:
    # 初始化信息，url，data
    @pytest.mark.parametrize("case", case_run_list)
    def test_case_run(self, case):
        case_key = ExcelConf.ExcelColumnConfig()
        case_url = ConfigYaml().get_conf_host_url() + case[case_key.case_url]
        case_id = case[case_key.case_id]
        case_model = case[case_key.case_model]
        case_name = case[case_key.case_name]
        case_precondition = case[case_key.case_precondition]
        case_method = case[case_key.case_method]
        case_params_type = case[case_key.case_params_type]
        case_params = case[case_key.case_params]
        case_expect_result = case[case_key.case_expect_result]
        case_content = case[case_key.case_content]
        case_headers = case[case_key.case_headers]
        case_cookies = case[case_key.case_cookies]
        case_code = case[case_key.case_code]
        case_db_verify = case[case_key.case_db_verify]

        # 如果headers存在，就转换成json格式
        if case_headers:
            headers = json.loads(case_headers)
        else:
            headers = case_headers
        # 如果cookies存在，就转换成json格式
        if case_cookies:
            cookies = json.loads(case_cookies)
        else:
            cookies = case_cookies

        if case_precondition:
            # 获取前置测试用例
            precondition = case_run_data.get_case_precondition(case_precondition)
            print("前置条件：%s"%precondition)
        # 接口请求，工具类
        req = Request()
        # params如果有内容，params转成json
        if len(str(case_params).strip()) is not 0:
            params = json.loads(case_params)
        else:
            params = case_params
        # 判断方法
        if str(case_method).lower() == "get":
            res = req.get(url=case_url, json=params, headers=headers, cookies=cookies)
        elif str(case_method).lower() == "post":
            res = req.post(url=case_url, json=params, headers=headers, cookies=cookies)
        else:
            log.error("错误的请求类型，method：%s" % case_method)
            res = None
        print(res)
        assert res == case_expect_result
        sleep(5)


# TestExcelCase().test_case_run()

if __name__ == '__main__':
    pytest.main(["-s","test_excel_case.py"])