# -*- coding:utf-8 -*-
"""
@author: Alan
@file: test_write.py
@time: 2023/3/8 18:36
@desc: 
"""
from config import Conf
from utils.RequestsUtil import Request
from utils.YamlUtil import YamlReader
import os
import pytest

# 1.获取测试用例列表
# 获取datayaml文件路径，读取多个文档
# 2.参数化

# 获取文件路径
test_file = os.path.join(Conf.get_data_path(), "test_write.yml")
# 读取文件内容
data_list = YamlReader(test_file).data_all()


@pytest.mark.parametrize("data_one", data_list)
def test_write(data_one):
    url = data_one["url"]
    data = data_one["data"]
    req = Request()
    res = req.post(url=url,json=data)
    print(res)

if __name__ == '__main__':
    pytest.main(["-s","test_write.py"])
