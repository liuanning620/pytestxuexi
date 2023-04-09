# -*- coding:utf-8 -*-
"""
@author: Alan
@file: Base.py
@time: 2023/3/8 16:26
@desc: 
"""
import json
import logging
import os
import re
import subprocess

from config import Conf
from config.Conf import ConfigYaml
from utils.LogUtil import my_log
from utils.MysqlUtil import Dbmysql
from utils.AssertUtil import AssertUtil

log = my_log()

# 初始化数据库信息，配置文件conf_db.yml
def init_db(db_name):
    conf_db_info = ConfigYaml().get_conf_db_info(db_name)
    host = conf_db_info["db_host"]
    user = conf_db_info["db_user"]
    passwprd = conf_db_info["db_password"]
    database = conf_db_info["db_database"]
    charset = conf_db_info["db_charset"]
    port = int(conf_db_info["db_port"])
    conn = Dbmysql(host=host,user=user,password=passwprd,database=database,charset=charset,port=port)
    return conn

# 用列表推导式，定义方法：判断参数是否存在，存在转换成json格式
def json_data(data):
    # if data:
    #     cookies = json.loads(data)
    # else:
    #     cookies = data
    # data存在返回json.loads(data),如果data不存在，返回data，相当于注释上面的
    return json.loads(data) if data else data

# 定义查询，替换的公共方法
# 验证亲戚是否存在${}$，存在返回${}$中的内容
# 关联方法

# 查询方法,返回${}$中的值
def reslut_re_find(data, pattern_str='\${(.*)}\$'):
    # 正则匹配，匹配{}里面是否存在 ---任意字符*任意个数*，用括号括起来，pattern.findall（）输出的值是列表
    '''

    :param data: 包含${}$的字符串，如：'{"Token":"${token}$"}'
    :param pattern_str: 匹配格式，默认值：'\${(.*)}\$', 用来提取${}$中的内容
    :return: 返回${}$中的内容，列表，['token']
    '''

    # pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_str)
    res = pattern.findall(data)
    print("调用查询方法reslut_re_find(),返回${}$中的key: %s"%res)
    return res

# 替换方法，把${}$中的值，替换成想要的值，如替换成前置用例的输出值
def reslut_re_replace(data, replace_str, pattern_str='\${(.*)}\$'):
    '''

    :param data: 包含${}$的字符串，如：'{"Token":"${token}$"}'
    :param replace_str:需要被替换的值，如"abc123",则替换后，'{"Token":"abc123"}'
    :param pattern_str: 匹配格式，默认值：'\${(.*)}\$', 用来提取${}$中的内容
    :return: 替换后的字符串，如'{"Token":"abc123"}'
    '''

    pattern = re.compile(pattern_str)
    res = pattern.findall(data)
    if res:
        result = re.sub(pattern_str,replace_str,data)
        print("调用替换方法reslut_re_replace()，把${}$中的值：%s，替换成想要的值:%s，如替换成前置用例的输出值: %s"%(res, replace_str, result))
        return result

# 查询请求中是否有需要${关联的信息
def params_find_pattern(headers,cookies):
    if "${" in headers:
        headers = reslut_re_find(headers)
    if "${" in headers:
        headers = reslut_re_find(headers)
    return headers, cookies


def assert_db_verify(db_name, case_result, case_db_verify):
    assert_util = AssertUtil()
    sql = init_db(db_name)
    db_res = sql.fetchone(case_db_verify)
    log.debug("数据库查询结果：{}".format(str(db_res)))
    verify_list = list(dict(db_res).keys())
    for line in verify_list:
        res_line = case_result[line]
        res_db_line = dict(db_res)[line]
        assert_util.assert_body(res_line,res_db_line)

# print(reslut_re_find('{"Token":"${token}$"}'))
# print(reslut_re_replace('{"Token":"${token}$"}','abc123'))

def allure_report_html(report_result_path, report_html_path):
    allure_cmd = "allure generate {} -o {} --clean".format(report_result_path, report_html_path)
    log.info("生成html报告")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败")
        raise

# report_result_path = Conf.get_report_path() + os.sep + "result"
# report_html_path = Conf.get_report_path() + os.sep + "html"
#
# allure_report_subprocess(report_result_path, report_html_path)



