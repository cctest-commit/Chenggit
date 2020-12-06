#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [4, 5])
def test_param(a, b):
    print(a, b)
