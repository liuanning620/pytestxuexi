# -*- coding:utf-8 -*-
"""
@author: Alan
@file: YamlUtil.py
@time: 2023/3/7 16:36
@desc: yaml方法
"""
import os
import yaml


class YamlReader:
    # 初始化
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None
    # 读取单个文件
    def data(self):
        # 第一次调用data，读取yaml，不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
        return self._data
    # 读取多个文档
    def data_all(self):
        # 第一次调用data，读取yaml，不是，直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all
