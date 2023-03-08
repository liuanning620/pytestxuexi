# -*- coding:utf-8 -*-
"""
@author: Alan
@file: log_file_demo.py
@time: 2023/3/7 18:44
@desc: 
"""

'''
%(levelno)s-------日志级别的数值
%(levelname)s-------日志级别的名称
%(pathname)s-------当前执行程序的路径，其实就是sys.argv[0]
%(filenmae)s-------当前执行的程序名
%(funcName)s-------日志当前函数
%(lineno)d-------日志当前行号
%(asctime)s-------日志时间
%(thread)d-------线程ID
%(threadName)s-------线程名称
%(process)d-------进程ID
%(message)s-------日志信息
'''


import logging
# 输出控制台

# 设置logger名称
logger = logging.getLogger("log_file_demo")
# 设置log级别
logger.setLevel(logging.DEBUG)
# 创建handler
# 输出到文件
fh_file = logging.FileHandler("./test.log")
# 输出到控制台
fh_stream = logging.StreamHandler()
# 设置日志级别
fh_stream.setLevel(logging.INFO)
fh_file.setLevel(logging.DEBUG)
# 定义输出格式
formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
# 添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
# 运行输出
logger.info("this is info")
logger.debug("this is debug")
logger.warning("this is warning")

