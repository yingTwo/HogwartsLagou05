import pytest

#在测试用例中，用的话，就再方法中传fixture装饰的方法的名字
# @pytest.fixture(scope="class")
# def connectDB():
#     print("连接数据库")
#     yield
#     print("断开数据库")

class TestDemo:
    def test_case1(self, connectDB):
        print("测试用例a")


    def test_case2(self):
        print("测试用例b")

class TestDemo2:
    def test_case12(self, connectDB):
        print("测试用例a2")


    def test_case22(self, connectDB):
        print("测试用例b2")