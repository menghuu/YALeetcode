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
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            num = nums[i]
            next_position = i + num
            if next_position >= len(nums) - 1:
                return True
            for j in range(i + 1, next_position):
                if nums[j] + j > nums[next_position] + next_position:
                    next_position = j
            if nums[next_position] == 0:
                return False
            else:
                i = next_position
        return True
