import pytest
import yaml

from HomeWorkYing.Pytestfirst.calculator import Calculator
  #注：此测试文件中，测试数据有异常用例的数据，会有测试不通过的情况，为正常现象。

class TestCal:
    def setup_class(self):
        self.cal = Calculator()

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    '''#方式一：
    @pytest.mark.skip
    # @pytest.mark.parametrize("a,b,excepted", [(3, 4, 5), (9, 3, 6)])   #直接参数化
    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("./cal_data.yml"))["sub_datas"])  # 用文件中数据做参数
    def test_sub(self, a, b, excepted):
        result = self.cal.sub(a, b)
        assert result == excepted

    @pytest.mark.skip
    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("./cal_data.yml"))["mul_datas"])
    def test_mul(self, a, b, excepted):
        result = self.cal.mul(a, b)
        assert result == excepted

    @pytest.mark.parametrize("a,b,excepted", yaml.safe_load(open("./cal_data.yml"))["div_datas"])
    def test_div(self, a, b, excepted):
        result = self.cal.div(a, b)
        assert result == excepted
    '''
    # 方式二：
    def get_datas():
        with open("C:/Users/zhy/PycharmHgworts5/HomeWorkYing/Pytestfirst/cal_data.yml") as f:
            datas = yaml.safe_load(f)
            add_datas = datas["add_datas"]
            sub_datas = datas["sub_datas"]
            mul_datas = datas["mul_datas"]
            div_datas = datas["div_datas"]
            return [add_datas, sub_datas, mul_datas, div_datas]

    def get_result(self, a, b):
        add_result = self.cal.add(a, b)
        sub_result = self.cal.sub(a, b)
        mul_result = self.cal.mul(a, b)
        div_result = self.cal.div(a, b)
        return [add_result, sub_result, mul_result, div_result]

    @pytest.mark.parametrize("a,b,excepted", get_datas()[0])
    def test_add(self, a, b, excepted):
        assert self.get_result(a, b)[0] == excepted

    @pytest.mark.parametrize("a,b,excepted", get_datas()[1])
    def test_sub(self, a, b, excepted):
        assert self.get_result(a, b)[1] == excepted


    @pytest.mark.parametrize("a,b,excepted", get_datas()[2])
    def test_mul(self, a, b, excepted):
        assert self.get_result(a, b)[2] == excepted

    @pytest.mark.parametrize("a,b,excepted", get_datas()[3])
    def test_div(self, a, b, excepted):
        assert self.get_result(a, b)[3] == excepted

