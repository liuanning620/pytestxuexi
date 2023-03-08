# -*- coding:utf-8 -*-
"""
@author: Alan
@file: Conf.py.py
@time: 2023/3/7 17:34
@desc: 
"""
import os
from utils.YamlUtil import YamlReader
# 获取项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
# 定义conf.yml文件的路径
_config_yaml_file = _config_path + os.sep + "conf.yml"
# 定义输出log文件目录的路径
_config_log_path = BASE_DIR + os.sep + "logs"
# 定义db_conf.yml路径
_config_db_yaml_file = _config_path + os.sep + "conf_db.yml"
# 获取配置文件路径
def get_config_path():
    return _config_path

# 获取yaml文件路径
def get_config_yaml_file():
    return _config_yaml_file

# 获取log文件的路径
def get_config_log_path():
    return _config_log_path

# 获取log文件的路径
def get_config_db_file():
    return _config_db_yaml_file

# 读取配置文件
# 1.创建类
class ConfigYaml:
    # 初始化，yaml读取配置文件
    def __init__(self):
        # 读取conf.yml文件
        self.config = YamlReader(get_config_yaml_file()).data()
        self.config_db = YamlReader(get_config_db_file()).data()
        # 定义方法获取需要的信息
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]
    # 定义方法，获取log文件的日志级别
    def get_conf_log_level(self):
        return self.config["BASE"]["log_level"]
    # 定义方法，获取log文件的扩展名
    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    # 定义方法，根据数据库名称，获取数据库配置信息
    def get_conf_db_info(self,db_name):
        return self.config_db[db_name]

# if __name__ == '__main__':
#     conf_read = ConfigYaml()
#     print(conf_read.get_conf_db_info("db_2"))
#     print(conf_read.get_conf_url())
#     print(conf_read.get_conf_log_level())
#     print(conf_read.get_conf_log_extension())