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
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if not prices:
            return 0

        if k > len(prices) // 2:
            # 这里就相当于k为无限制的时候的解法
            for i in range(len(prices)):
                price = prices[i]
                if i == 0:
                    dps = [0, -price]
                else:
                    dps = [
                        max(dps[0], dps[1] + price),
                        max(dps[1], dps[0] - price)
                    ]
            return dps[0]

        dps = [[[0, 0] for _ in range(k + 1)] for _ in prices]

        for i in range(len(prices)):
            price = prices[i]
            for j in range(1, k + 1):
                if i == 0:
                    dps[i][j][0] = 0
                    dps[i][j][1] = -price
                else:
                    dps[i][j][0] = max(dps[i - 1][j][0], dps[i - 1][j][1] + price)
                    # dps[...][0][0] 一定等于 0
                    dps[i][j][1] = max(dps[i - 1][j][1], dps[i - 1][j - 1][0] - price)

        return dps[-1][-1][0]
