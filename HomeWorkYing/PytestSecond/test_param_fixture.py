import pytest


@pytest.fixture(params=[1, 2, 3], ids=["r1", "r2", "r3"])
def login1(request):
    data = request.param
    return data + 4

def test_case1(login1):
    print("ceshiyongli1")
    print(f"获取测试数据：{login1}")