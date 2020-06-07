#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
dps更新的时候，不包含nums[i]的时候，需要取一个max
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dps = [[0, 0]]
        for i in range(len(nums)):
            num = nums[i]
            dps.append([
                max(dps[-1][1], dps[-1][0]), 
                dps[-1][0] + num
            ])
        return max(dps[-1])

