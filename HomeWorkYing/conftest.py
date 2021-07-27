import os
import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# print(sys.path)
# sys.path.append("C:\\Users\\zhy\\LGHomeworkUpload")

from typing import List

import pytest

from HogwartsLagou05.HomeWorkYing.PytestSecond.calculator import Calculator


import yaml


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")

def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')



yaml_file_path = os.path.dirname(__file__) + "/PytestSecond/data.yml"
# yaml_file_path = os.path.dirname(__file__) + "/data.yml"
with open(yaml_file_path, "r", encoding="utf-8") as f:
    datasa = yaml.safe_load(f)
    print(datasa)
    datas = datasa["datas"]
    ids = datasa["ids"]


@pytest.fixture(scope="module")
def get_cal():
    print("获取计算机实例")
    cal = Calculator()
    return cal


@pytest.fixture(params=datas["a_datas"], ids=ids["a_ids"])
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("计算结束")

@pytest.fixture(params=datas["d_datas"], ids=ids["a_ids"])
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("计算结束")

@pytest.fixture(params=datas["s_datas"], ids=ids["a_ids"])
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("计算结束")
@pytest.fixture(params=datas["m_datas"], ids=ids["a_ids"])
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("计算结束")


