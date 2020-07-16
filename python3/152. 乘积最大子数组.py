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
    def maxProduct(self, nums: List[int]) -> int:
        dps = [[1, 1]]
        ans = float('-inf')
        for num in nums:
            max_ = max(num * dps[-1][0], num * dps[-1][1], num)
            min_ = min(num * dps[-1][0], num * dps[-1][1], num)
            dps.append([max_, min_])
            ans = max(max_, ans)

        return ans
