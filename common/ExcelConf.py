# -*- coding:utf-8 -*-
"""
@author: Alan
@file: ExcelConf.py.py
@time: 2023/3/9 14:41
@desc: 
"""

# excel与文件列的映射关系
class ExcelColumnConfig:
    case_id = "用例ID"
    case_model = "模块"
    case_name = "接口名称"
    case_url = "url"
    case_precondition = "前置条件"
    case_method = "请求类型"
    case_params_type = "请求参数类型"
    case_params = "请求参数"
    case_expect_result = "预期结果"
    case_actual_result = "实际结果"
    case_content = "备注"
    case_is_run = "是否运行"
    case_headers = "headers"
    case_cookies = "cookies"
    case_code = "status_code"
    case_db_verify = "数据库验证"