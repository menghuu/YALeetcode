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
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return  0

        dps = [[0, 0] for _ in prices]

        for i in range(len(prices)):
            price = prices[i]
            if i == 0:
               dps[i][0] = 0
               dps[i][1] = -price
            else:
                dps[i][0] = max(dps[i - 1][0], dps[i - 1][1] + price)

                if i - 2 >= 0:
                    dps[i][1] = max(dps[i - 1][1], dps[i - 2][0] - price)
                else:
                    dps[i][1] = max(dps[i - 1][1], -price)
        return dps[-1][0]
