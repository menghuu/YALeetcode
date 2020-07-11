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
    def coinChange(self, coins: List[int], amount: int) -> int:
        dps = [float('inf') for _ in range(amount + 1)]
        dps[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dps[i] = min(dps[i], dps[i - coin] + 1)

        import math

        return -1 if math.isinf(dps[-1]) else dps[-1]
