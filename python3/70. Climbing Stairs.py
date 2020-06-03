#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
斐波那契数列
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n + 1):
            b, a = a + b, b
        return b
