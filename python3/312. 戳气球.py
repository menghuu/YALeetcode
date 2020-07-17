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
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        # dps[i][j] 以 (i, j)为边界的最大的硬币和
        dps = [[0 for _ in nums] for _ in nums]
        for left in range(len(nums) - 2, -1, -1):
            for right in range(left + 2, len(nums)):
                for i in range(left + 1, right):
                    dps[left][right] = max(
                        dps[left][right],
                        dps[left][i] + dps[i][right] + nums[left] * nums[i] * nums[right]
                    )

        return dps[0][len(nums) - 1]

        nums = [1] + nums + [1]
        from functools import lru_cache
        @lru_cache(None)
        def dp_fn(left, right):
            if left + 1 == right:
                return 0
            else:
                m = max(
                    nums[left] * nums[i] * nums[right] + dp_fn(left, i) + dp_fn(i, right)
                    for i in range(left + 1, right)
                )
                return m

        return dp_fn(0, len(nums) - 1)
