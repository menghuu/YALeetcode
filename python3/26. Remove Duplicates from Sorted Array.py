#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
又是双指针，要充分利用有序性，如果有i <= j，则必然有nums[i] <= nums[j]
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
