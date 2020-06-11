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
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        while left <= right:
            middle = (left + right) // 2
            t = middle ** 2
            if t <= x:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1

        return ans
