# -*- coding:utf-8 -*-
"""
@author: Alan
@file: demo-suprocess.py
@time: 2023/4/1 9:11
@desc: 
"""
import subprocess
x = subprocess.call("allure generate report/result -o report/html --clean", shell=True)
print(x)