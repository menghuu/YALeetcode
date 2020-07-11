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
    def numSquares(self, n: int) -> int:
        dps = [float('inf') for _ in range(n + 1)]
        dps[0] = 0

        for i in range(n + 1):
            num = i ** 2
            if num > n:
                break
            for i in range(num, n + 1):
                ii = i - num
                dps[i] = min(dps[i], dps[ii] + 1)

        import math
        ans = 0 if math.isinf(dps[-1]) else dps[-1]
        return ans
