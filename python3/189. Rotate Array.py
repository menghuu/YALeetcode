#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
第一种做法最困难的是结束条件，那个count很重要
第二种做法确实有些神奇，先全部反转之后，再反转前K个，然后再反转后面的那些
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.rotate2(nums, k)
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            prev = nums[start]
            index = (start + k) % len(nums)
            while True:
                nums[index], prev = prev, nums[index]
                count += 1
                if index == start:
                    break
                index = (index + k) % len(nums)
            start += 1
        
    def rotate2(self, nums, k):
        k = k % (len(nums))
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(k):
            j = k - 1 - i
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(len(nums) - k):
            j = len(nums) - k - i - 1
            if i >= j:
                break
            i = i + k
            j = j + k
            nums[i], nums[j] = nums[j], nums[i]
