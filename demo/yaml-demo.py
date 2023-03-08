# -*- coding:utf-8 -*-
"""
@author: Alan
@file: yaml-demo.py
@time: 2023/3/7 11:05
@desc: yaml-demo
"""
from utils.YamlUtil import YamlReader

# res = YamlReader("./yamldemo.yml").data()
res = YamlReader("./yamldemo.yml").data_all()
print(res)