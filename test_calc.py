#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from pythoncode.calculator import Calculator
import pytest


def test_a():
    print("这是计算测试用例")


# 解析测试数据文件：
def get_datas():
    with open("./datas/calc.yml", encoding="utf-8")as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]["datas"]
        add_ids = datas["add"]["ids"]
        div_datas = datas["div"]["datas"]
        div_ids = datas["div"]["ids"]
        sub_datas = datas["sub"]["datas"]
        sub_ids = datas["sub"]["ids"]
        mul_datas = datas["mul"]["datas"]
        mul_ids = datas["mul"]["ids"]
        return [add_datas, add_ids, div_datas, div_ids, sub_datas, sub_ids, mul_datas, mul_ids]


# # 解析测试步骤文件
# def steps(calc, a, b, expect):
#     with open("./steps/add_steps.yml")as f:
#         steps = yaml.safe_load(f)
#     for step in steps:
#         if step == "add":
#             resault = calc.add(a, b)
#         else:
#             resault = calc.add1(a, b)
#     assert resault == expect


class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()

    #     不用self的话就是局部变量，采用self.cale 变成类变量

    # def setup(self):
    #     print("计算开始")
    #
    # def teardown(self):
    #     print("计算结束")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, expect", get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, a, b, expect):
        resault = get_calc.add(a, b)
        assert round(resault, 1) == round(expect, 1)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expect", get_datas()[2], ids=get_datas()[3])
    def test_div(self, get_calc, a, b, expect):
        if b != 0:
            resault = get_calc.div(a, b)
            assert round(resault, 2) == round(expect, 2)
        else:
            try:
                get_calc.div(1, 0)
            except Exception:
                print("除数为0")
        #     with pytest.raises(ZeroDivisionError):
        #         print("除数为01")
        #         expect = self.calc.div(1, 0)
        #         print("除数为02")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_datas()[4], ids=get_datas()[5])
    def test_sub(self, get_calc, a, b, expect):
        resault = get_calc.sub(a, b)
        assert round(resault, 1) == round(expect, 1)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_datas()[6], ids=get_datas()[7])
    def test_mul(self, get_calc, a, b, expect):
        resault = get_calc.mul(a, b)
        assert round(resault, 1) == round(expect, 1)

    # def test_add_steps(self,get_calc,):
    #     # assert 2==self.calc.add(1,1)
    #     # assert 3==self.calc.add1(1,2)
    #     # assert 0==self.calc.add(-1,1)
    #     a = 1
    #     b = 1
    #     expect = 2
    #     steps(get_calc, a, b, expect)
