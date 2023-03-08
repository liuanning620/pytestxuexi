# -*- coding:utf-8 -*-
"""
@author: Alan
@file: LogUtil.py
@time: 2023/3/8 8:06
@desc: 封装Log工具类
"""
import logging
import datetime
import os
from config import Conf
from config.Conf import ConfigYaml

# 定义日志级别映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}


class Logger:
    # 定义参数：日志名称，日志级别，输出文件名称
    def __init__(self, log_file, log_name, log_level):
        # 扩展名可以放到日志配置文件里
        self.log_file = log_file
        # 参数，不需要放入配置文件
        self.log_name = log_name
        # 放入配置文件
        self.log_level = log_level

        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])
        # 判断handler是否存在
        # 创建输出到控制台的handler
        if not self.logger.handlers:
            fh_stream = logging.StreamHandler()
            # 设置日志级别
            fh_stream.setLevel(log_l[self.log_level])
            # 定义输出格式
            formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')
            # 输出到控制台
            fh_stream.setFormatter(formatter)

            # 创建输出到文件的handler
            fh_file = logging.FileHandler(log_file)
            # 设置日志级别
            fh_file.setLevel(log_l[self.log_level])
            # 定义输出格式，上面已经定义了格式，直接使用
            # 输出到文件
            fh_file.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 1.初始化参数数据，日志文件名称，日志文件级别
# 日志文件名称 = logs目录+当前时间+扩展名
# 获取logs目录D:\WorkSoftware\PycharmProjects\pytestxuexi\logs
log_path = Conf.get_log_path()
# 获取当期前时间2023-03-08
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# 获取日志扩展名.log
log_extenison = ConfigYaml().get_conf_log_extension()
# 拼接，存放日志D:\WorkSoftware\PycharmProjects\pytestxuexi\logs\2023-03-08.log
log_file = os.path.join(log_path, current_time + log_extenison)
# 获取日志级别
log_level = ConfigYaml().get_conf_log_level()


# 2.对外方法，初始化log工具类，提供其他类使用
def my_log(log_name=__file__):
    return Logger(log_file=log_file, log_name=log_name, log_level=log_level).logger

#
# if __name__ == "__main__":
#     my_log().debug("this is debug info")
