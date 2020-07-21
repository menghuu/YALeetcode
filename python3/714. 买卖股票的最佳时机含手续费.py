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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        for i in range(len(prices)):
            price = prices[i]
            if i == 0:
                dp = [0, -price]
            else:
                dp = [
                    max(dp[0], dp[1] + price - fee),
                    max(dp[1], dp[0] - price)
                ]
        
        return max(dp)
