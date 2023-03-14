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
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
from common import ExcelConf, Base
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

# 获取配置方法中列的名字
case_key = ExcelConf.ExcelColumnConfig()


# 执行用例
# 1.增加pytest，修改方法参数，重构函数内容，pytest.main运行
class TestExcelCase:

    # 提取前置和运行用例的公共方法,发送请求的api
    def case_public_func(self, url, method, params=None, headers=None, cookies=None):
        # 接口请求，工具类
        req = Request()
        # params如果有内容，params转成json
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        else:
            params = params
        # 判断方法
        if str(method).lower() == "get":
            res = req.get(url=url, json=params, headers=headers, cookies=cookies)
        elif str(method).lower() == "post":
            res = req.post(url=url, json=params, headers=headers, cookies=cookies)
        else:
            log.error("错误的请求类型，method：%s" % method)
            res = None
        return res

    # 执行前置用例方法,获得返回结果
    def run_case_precondition(self, precondition_case):
        print("调用执行前置用例方法run_case_precondition()")
        case_url = ConfigYaml().get_conf_host_url() + precondition_case[case_key.case_url]
        case_method = precondition_case[case_key.case_method]
        case_params = precondition_case[case_key.case_params]
        case_headers = precondition_case[case_key.case_headers]
        case_cookies = precondition_case[case_key.case_cookies]

        # 如果headers存在，就转换成json格式
        headers = Base.json_data(case_headers)
        # 如果cookies存在，就转换成json格式
        cookies = Base.json_data(case_cookies)
        # 调用公共方法：请求
        res = self.case_public_func(url=case_url, method=case_method, params=case_params, headers=headers,
                                    cookies=cookies)
        print("前置用例执行结果：%s"%res)
        return res

    # 初始化信息，url，data
    @pytest.mark.parametrize("case", case_run_list)
    def test_case_run(self, case):
        print("调用方法test_case_run(),parametrize获取所有需要运行的用例")
        # case_key = ExcelConf.ExcelColumnConfig()
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
        headers = Base.json_data(case_headers)
        # 如果cookies存在，就转换成json格式
        cookies = Base.json_data(case_cookies)

        if case_precondition:
            # 获取前置测试用例
            precondition = case_run_data.get_case_precondition(case_precondition)
            print("存在前置条件，获取前置用例的case所有信息，前置用例执行结果如下")
            # print("前置条件：%s" % precondition)
            res_precoondition = self.run_case_precondition(precondition)
            header, cookie = self.get_correlation(headers, cookies, res_precoondition)
            sleep(5)
            # 如果headers存在，就转换成json格式
            headers = Base.json_data(header)
            # 如果cookies存在，就转换成json格式
            cookies = Base.json_data(cookie)
        # 调用公共方法：请求
        # res = self.case_public_func(url=case_url, method=case_method, params=case_params, headers=headers,
        #                             cookies=cookies)
        # print("需要运行的用例执行结果：%s"%res)
        # assert_util = AssertUtil()
        # assert_util.assert_code(int(res['code']), int(case_code))
        # sleep(5)


# TestExcelCase().test_case_run()


    # 验证是否有关联，有执行前置用例，获取结果，结果替换
    def get_correlation(self, headers, cookies, res_precoondition):
        headers_param, cookies_param = Base.params_find_pattern(headers, cookies)
        if len(headers_param):
            headers_data = res_precoondition["body"][headers[0]]
            headers_param = Base.reslut_re_replace(headers,headers_data)
            print("如果headers中存在${,获取，替换侯的内容")
        if len(cookies_param):
            cookies_data = res_precoondition["body"][cookies_param[0]]
            cookies_param = Base.reslut_re_replace(cookies_param,cookies_data)
            print("如果cookies中存在${,获取，替换侯的内容")
        return headers_param, cookies_param

if __name__ == '__main__':
    # pytest.main(["-s", "test_excel_case.py"])

    import re
    str1 = '{"Authorization":"JWT${token}$"}'
    pattern = re.compile('\${(.*)}\$')
    res = pattern.findall(str1)
    token = "123"
    a = re.sub(pattern,token,str1)
    print(a)