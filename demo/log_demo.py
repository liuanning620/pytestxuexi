#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Alan
@file: log_demo.py
@time: 2023/3/7 18:37
@desc: 
"""
import logging
# 设置配置信息
logging.basicConfig(level=logging.INFO,format='%(asctime)s--%(name)s--%(levelname)s-%(message)s')
# 定义日志名称getlogger,名称log-demo
logger = logging.getLogger("log_demo")
logger.info("info_msg")
logger.debug("debug_msg")