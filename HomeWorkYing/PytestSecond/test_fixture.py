import pytest

#不同测试用例有不同的初始化需求的时候，可以用fixture，
#fixture相当于pytest的一个外壳函数，可以模拟setup和teardown的操作
#yield之前的操作相当于setup，yield之后的操作相当于teardown
#yield有return功能，若需要返回数据，直接放在yield后面
# fixture可以模拟setup和teardown，用yield 可以模拟teardown

@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = "tom"
    age = 18
    token = "token 123456"
    yield [username, age, token]
    print("登出操作")


#测试用例1：需要登录
def test_case1(login):
    m = login
    print(m[0])
    print(f"返回数据是：{login}")
    print("测试用例1")

#测试用例2：不需要登录
def test_case2(connectDB):
    print("测试用例2")


# 测试用例3：需要登录
def test_case3(login):
    print("测试用例3")


# 测试用例4：需要登录(用另一种fixture用法)
#pytest.mark.usefixtures("login")括号中的内容一定是字符串内容，是fixture修饰的方法名字
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")

@pytest.mark.parametrize("name",["張三", "李四"])
def test_mm(name):
    print(name)