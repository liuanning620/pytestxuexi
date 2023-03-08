# -*- coding:utf-8 -*-
"""
@author: Alan
@file: Base.py
@time: 2023/3/8 16:26
@desc: 
"""
from config.Conf import ConfigYaml
from utils.MysqlUtil import Dbmysql

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
# print(init_db("db_1"))