# -*- coding:utf-8 -*-
"""
@author: Alan
@file: ExcelData.py
@time: 2023/3/9 11:05
@desc: 
"""

from utils.ExcelUtil import ExcelReader
from common.ExcelConf import ExcelColumnConfig

# 1.使用excel工具类，获取所有数据
# 2.判断是否运行
# 3.保存执行结果，放入新表


class CaseExcelRunData:
    def __init__(self, excel_case_file, excel_sheet_name):
        # self.reader_excel_all = ExcelReader("../data/api.xlsx","Sheet1")
        self.reader_excel_all = ExcelReader(excel_case_file,excel_sheet_name)

    # 获取所有数据
    def get_excel_all_data(self):
        # run_list = list()
        # for line in self.reader_excel_all.data():
        #     run_list.append(line)
        # 列表推导式，可以代替上面的的注释代码
        run_list = [line for line in self.reader_excel_all.data()]
        return run_list

    # 根据前置条件中的用例id找到前置用例的所在行信息
    def get_case_precondition(self, precondition):
        # 获取全部测试用例，list判断执行获取
        case_all_list = self.get_excel_all_data()
        for line in case_all_list:
            if precondition in dict(line).values():
                print("存在前置用例：%s"%line['用例ID'])
                return line
        return None

    # 获取运行的所有数据
    def get_excel_run_data(self):
        run_list = list()
        for line in self.reader_excel_all.data():
            if str(line[ExcelColumnConfig.case_is_run]).lower() == 'y':
                run_list.append(line)
        print("需要执行的用例：%s"%run_list)
        return run_list

#
# if __name__ == '__main__':
#     reader_excel_all = CaseExcelRunData("../data/api.xlsx","Sheet1")
#     reader_excel_all.get_excel_run_data()
