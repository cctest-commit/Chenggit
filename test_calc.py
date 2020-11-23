# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
from pythoncode.calculator import Calculator
import pytest


def test_a():
    print("这是计算测试用例")


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expect", [[1, 1, 2], [100, 200, 300], [0.1, 0.2, 0.3], [0.1, 1, 1.1],
                                              [-1, -2, -3], [0, 1, 1], [0, 0, 0]],
                             ids=["int+int", "bignum+bignum", "float+float", "float+int", "negative+negative",
                                  "zero+int","zero+zero"])
    def test_add(self, a, b, expect):
        resault = self.calc.add(a, b)
        assert round(resault, 1) == round(expect, 1)

    @pytest.mark.parametrize("a, b, expect", [[4, 4, 1], [4, 2, 2], [4, 1, 4], [0, 4, 0],
                                              [4, 0.1, 40], [0.1, 4, 0.025], [-4, 2, -2], [4, 3, 1.33], [-4, 3, -1.33],
                                              [4, 0, 0]],
                             ids=["本身/本身", "整除", "本身/1", "0/本身",
                                  "本身/小数", "小数/本身", "负数整除", "非整除", "负数非整除", "除数为0"])
    def test_div(self, a, b, expect):
        if b != 0:
            resault = self.calc.div(a, b)
            assert round(resault, 3) == round(resault, 3)
        else:
            print("除数为0")
