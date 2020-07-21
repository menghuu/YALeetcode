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
        dps = []
        for price in prices:
            if not dps or price <= dps[-1]:
                dps.append(price)
            else:
                dps.append(dps[-1])
        ans = 0
        for buy, sold in zip(dps[:-1], prices[1:]):
            ans = max(sold - buy, ans)
        return ans
            
