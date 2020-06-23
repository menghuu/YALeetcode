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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.productExceptSelf2(nums)
        
        dps1 = [1]
        dps2 = [1]
        for num in nums:
            dps1.append(dps1[-1] * num)
        dps1 = dps1[:-1]

        for num in nums[::-1]:
            dps2.append(dps2[-1] * num)
        dps2 = dps2[::-1][1:]

        ans = []
        for n1, n2 in zip(dps1, dps2):
            ans.append(n1 * n2)

        return ans
        
    def productExceptSelf2(self, nums):
        dps1 = [1]
        for num in nums:
            dps1.append(dps1[-1] * num)
        l = len(nums)
        dps1 = dps1[:l]
        nums.append(1)
        pre = 1
        for i in range(l - 1, -1, -1):
            nums[i], pre = nums[i+1] * pre, nums[i]
        nums = nums[:l]
        dps2 = nums 
        for i in range(len(nums)):
            dps1[i] = dps1[i] * dps2[i]
        return dps1

        #     1,  2,  3, 4
        # 24, 24, 12, 4, 1
