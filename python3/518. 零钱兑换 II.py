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
    def change(self, amount: int, coins: List[int]) -> int:
        dps = [0 for _ in range(amount + 1)]
        dps[0] = 1

        for coin in coins[:]:
            for i in range(coin, amount + 1):
                ii = i - coin
                dps[i] += dps[ii]
        
        return dps[-1]
