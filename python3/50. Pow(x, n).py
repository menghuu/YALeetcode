#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
其实不是很好做，细节太多
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        base = x
        exp = n 
        ans = 1
        while exp:
            if exp % 2 == 1:
                ans *= base
            base = base * base
            exp //= 2
        
        return ans
