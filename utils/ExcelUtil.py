# -*- coding:utf-8 -*-
"""
@author: Alan
@file: ExcelUtil.py
@time: 2023/3/9 10:07
@desc: 
"""

import xlrd
import os

# 自定义异常
class SheetTypeError(Exception):
    pass

class ExcelReader:
    def __init__(self,excel_file, sheet_type):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_type = sheet_type
            self.data_list =[]
        else:
            raise FileNotFoundError("excel文件不存在")

    # 读取sheet方式：1.名称:str；2.索引:int
    def data(self):
        global sheet
        if not self.data_list:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_type) not in [str, int]:
                raise SheetTypeError("请输入int或者str类型内容")
            elif type(self.sheet_type) ==int:
                sheet = workbook.sheet_by_index(self.sheet_type)
            elif type(self.sheet_type) ==str:
                sheet = workbook.sheet_by_name(self.sheet_type)
        # 读取sheet内容，返回list，每个元素是字典，格式[{},{}]
        # 获取首行信息，遍历行，与首行组成字典，放在list中
        # 定义首行
            title = sheet.row_values(0)
            for col in range(1,sheet.nrows):
                col_value = sheet.row_values(col)
                self.data_list.append(dict(zip(title,col_value)))
        return self.data_list


# if __name__ == '__main__':
#     res = ExcelReader("../data/api.xlsx","Sheet1")
#     print(res.data())
