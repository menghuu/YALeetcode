#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        ans = 0
        if x < 0:
            positive = False
            x = -x
            MAX = 2 ** 31
        else:
            positive = True
            MAX = 2 ** 31 - 1
        base = 1
        while x // base:
            base *= 10
        base //= 10
        while x:
            n = (x % 10) * base
            delta = MAX - ans
            if delta < n:
                return 0
            ans += n
            base //= 10
            x //= 10
        return ans if positive else -ans
