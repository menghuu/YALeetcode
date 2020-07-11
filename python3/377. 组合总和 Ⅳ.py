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
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dps = [0 for _ in range(target + 1)]
        dps[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dps[i] += dps[i - num]

        return dps[-1]
