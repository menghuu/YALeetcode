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
        
        not_keep_profit = 0
        keep_profit = -prices[0]
        for price in prices[1:]:
            not_keep_profit = max(not_keep_profit, keep_profit + price)
            keep_profit = max(not_keep_profit - price, keep_profit)
        return not_keep_profit


        dps = [[0, 1] for _ in prices]
        # dps[i][0]表示第i天的时候，手中没有持有股票，它所能拥有的利润
        # dps[i][1]表示第i天的时候，手中持有股票，它所能拥有的利润

        for i in range(len(prices)):
            if i == 0:
                dps[i][0] = 0
                dps[i][1] = -prices[i]
            else:
                dps[i][0] = max(dps[i - 1][0], dps[i - 1][1] + prices[i])
                dps[i][1] = max(dps[i - 1][1], dps[i - 1][0] - prices[i])
        return dps[-1][0]
