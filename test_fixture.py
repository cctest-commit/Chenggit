#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.run(order=4)
def test_case1(login):
    print("用例1")
    print(login)


#     方法中使用的话必须将参数引进来
@pytest.fixture(autouse=True)
def login():
    print("登录操作")
    # yield 相当于return操作
    yield ["tom", "12345"]
    print("登出操作")


def test_case2():
    print("用例2")


@pytest.mark.run(order=-1)
def test_case3(conn_db):
    print(conn_db)
    print("用例3")


@pytest.mark.run(order=1)
def test_case4():
    time.sleep(3)
    print("测试用例4")
