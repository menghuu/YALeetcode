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
    def hammingWeight(self, n: int) -> int:
        if n < 0:
            m = -n
            # 将m 按位取反 并加1， 得到二进制补码表示
            n = (m ^ 0xffffff) + 1
        
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
