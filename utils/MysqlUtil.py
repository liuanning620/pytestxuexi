# -*- coding:utf-8 -*-
"""
@author: Alan
@file: MysqlUtil.py
@time: 2023/3/8 14:08
@desc: 
"""

import pymysql
from utils.LogUtil import my_log


class Dbmysql:
    def __init__(self,host,user,password,database,port=3306,charset='utf8'):
        self.log = my_log("MysqlUtil")
        self.db_conn = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            charset = charset,
            port = port
         )
            # 创建游标对象，添加括号内容，会输出字典，不然只会输出元组，元组嵌套元组
        self.db_cursor = self.db_conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行查询一条数据
    def fetchone(self, query):
        self.db_cursor.execute(query)
        return self.db_cursor.fetchone()

    # 执行查询多条数据
    def fetchall(self, query):
        self.db_cursor.execute(query)
        return self.db_cursor.fetchall()

    # 查询方法
    def db_execute(self, query):
        try:
            if self.db_conn and self.db_cursor:
                self.db_cursor.execute(query)
            self.db_conn.commit()
        except Exception as e:
            self.db_conn.rollback()
            self.log.error("数据库执行失败，原因：%s"%e)
            return False
        return True

    # 关闭游标对象
    def db_close_cursor(self):
        if self.db_cursor is not None:
            self.db_cursor.close()

    # 关闭数据库连接
    def db_close_conn(self):
        if self.db_conn is not None:
            self.db_conn.close()

#
# if __name__ == '__main__':
#     mysql = Dbmysql(
#                 host = "127.0.0.1",
#                 user = "root",
#                 password = "123456",
#                 database = "test"
#                 )
#     # query = "SELECT * FROM student"
#     # res = mysql.fetchall(query)
#     # print(res)
#     query = "UPDATE student SET age = 50 WHERE id = 4"
#     res = mysql.db_execute(query)
#     print(res)


