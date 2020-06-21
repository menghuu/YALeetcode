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
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dps = []
        ans = float('-inf')
        for num in nums:
            if len(dps) == 0:
                dps.append(num)
            else:
                if num > num + dps[-1]:
                    dps.append(num)
                else:
                    dps.append(num + dps[-1])
            ans = max(ans, dps[-1])
        return ans
