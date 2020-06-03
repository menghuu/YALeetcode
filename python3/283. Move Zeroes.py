#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
双指针，一个是i，指向最靠前的0的位置
一个是j，指向第一个不为0的位置，当然这个位置j一定要大于i
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                break
        for j in range(i, len(nums)):
            if nums[j] != 0:
                break 
        
        while j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
            while i < len(nums) and nums[i] != 0:
                i += 1
            while j <= i or j < len(nums) and nums[j] == 0:
                j += 1
