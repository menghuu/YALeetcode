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
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dps = [[0, nums[0]]]
        ans = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            dps.append([
                max(dps[-1]),
                dps[-1][0] + num
            ])
            ans = max(dps[-1][0], dps[-1][1], ans)
        return ans

