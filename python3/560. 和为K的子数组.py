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
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        ans = 0
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            ans += prefix_count[cur_sum - k]
            prefix_count[cur_sum] += 1

        return ans
