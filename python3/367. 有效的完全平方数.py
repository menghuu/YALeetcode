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
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        while left <= right:
            middle = (left + right) // 2
            t = middle ** 2
            if t == num:
                return True
            elif t < num:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
