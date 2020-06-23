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
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return 
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return 
        
        for left in range(len(nums)-2, -1, -1):
            if nums[left] < nums[left+1]:
                break
        if left == 0 and nums[0] >= nums[1]:
            for i in range(len(nums) // 2):
                nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
            return nums
        for right in range(len(nums)-1, left, -1):
            if nums[right] > nums[left]:
                break
        nums[left], nums[right] = nums[right], nums[left]

        nums[left+1:] = list(sorted(nums[left+1:]))

        return nums


