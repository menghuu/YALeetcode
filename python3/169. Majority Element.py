#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
投票算法虽然看上去简单，但是心智负担比较重
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.using_dac(nums)
        return self.using_counter(nums)
        counts = 0
        for num in nums:
            if counts == 0:
                candidate = num
            counts += 1 if num == candidate else -1
        return candidate

    def using_counter(self, nums):
        from collections import Counter
        cs = Counter(nums)
        m = 0
        ans = None
        for c in cs:
            if cs[c] >= m:
                ans = c
                m = cs[c]
        return ans
    
    def using_dac(self, nums):
        def dac(nums, start_index, end_index):
            if start_index == end_index:
                return nums[start_index]
            
            middle = (start_index + end_index) // 2
            lnum = dac(nums, start_index, middle)
            rnum = dac(nums, middle + 1, end_index)
            if lnum == rnum:
                return lnum
            else:
                lcounts = sum([1 for num in nums[start_index: end_index+1] if num == lnum])
                rcounts = sum([1 for num in nums[start_index: end_index+1] if num == rnum])
                if lcounts >= rcounts:
                    return lnum
                else:
                    return rnum
        return dac(nums, 0, len(nums)-1)

