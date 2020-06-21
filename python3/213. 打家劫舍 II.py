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
        def rob_fn(nums):
            dps = [[0, nums[0]]]
            ans = nums[0]
            for num in nums[1:]:
                dps.append([
                    max(dps[-1]),
                    dps[-1][0] + num
                ])
                ans = max(dps[-1][0], dps[-1][1], ans)
            return ans
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) in [2, 3]:
            return max(nums)

        # 0偷，则1不偷，最后一个也不能偷
        num = nums[0]
        m1 = num + rob_fn(nums[2:-1])
        # 0不偷，则1无所谓，最后一个也无所谓
        m2 = rob_fn(nums[1:])

        return max(m1, m2)
