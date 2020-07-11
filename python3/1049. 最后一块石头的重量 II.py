#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
难点在于初始化，以及那个更新的规则
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)

        target = s // 2

        dps = [0 for _ in range(target + 1)]
        if stones[0] <= target:
            for i in range(stones[0], len(dps)):
                dps[i] = stones[0]

        for stone in stones[1:]:
            for i in range(target, -1, -1):
                ii = i - stone
                if ii >= 0 and i >= dps[ii] + stone >= dps[i]:
                    dps[i] = dps[ii] + stone

        ans = s - dps[-1] * 2

        return ans
