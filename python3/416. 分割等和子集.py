#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
01背包问题
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s // 2

        dps = [False for _ in range(target + 1)]
        if nums[0] <= target:
            dps[nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target, -1, -1):
                if j == 0:
                    dps[j] = 0
                elif j - nums[i] >= 0:
                    dps[j] = dps[j] or dps[j - nums[i]]
                else:
                    dps[j] = dps[j]

        return dps[-1]

        dps = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        if nums[0] <= target:
            dps[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target + 1):
                if j == 0:
                    dps[i][j] = False
                else:
                    dps[i][j] = dps[i - 1][j]
                    if j - nums[i] >= 0:
                        dps[i][j] = dps[i][j] or dps[i - 1][j - nums[i]]

        return dps[-1][-1]

