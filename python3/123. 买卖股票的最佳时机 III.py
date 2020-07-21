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
            return 0
        for i in range(len(prices)):
            price = prices[i]
            if i == 0:
                dps_10 = 0
                dps_11 = -price
                dps_20 = 0
                dps_21 = -price
            else:
                dps_10 = max(dps_10, dps_11 + price)
                dps_11 = max(dps_11, -price)
                dps_20 = max(dps_20, dps_21 + price)
                dps_21 = max(dps_21, dps_10 - price)
        
        return dps_20

        if not prices:
            return 0
        dps = [[[0, 0] for _ in range(3)] for _ in prices]
        # dps[i][j][0] 表示在i天时，最多进行了j次买入操作时，并且手上一份股票都没有的情况下的利润

        for i in range(len(prices)):
            if i == 0:
                dps[0][1][0] = 0
                dps[0][1][1] = -prices[i]
                dps[0][2][0] = 0
                dps[0][2][1] = -prices[i]
            else:
                dps[i][1][0] = max(dps[i - 1][1][0], dps[i - 1][1][1] + prices[i])
                dps[i][1][1] = max(dps[i - 1][1][1], - prices[i])
                dps[i][2][0] = max(dps[i - 1][2][0], dps[i - 1][2][1] + prices[i])
                dps[i][2][1] = max(dps[i - 1][2][1], dps[i - 1][1][0] - prices[i])

        return dps[-1][-1][0]

