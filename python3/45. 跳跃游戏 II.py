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
    def jump(self, nums: List[int]) -> int:
        i = 0
        steps = 0
        while i < len(nums) - 1:
            num = nums[i]
            steps += 1

            next_position = num + i
            if next_position >= len(nums) - 1:
                return steps 
            for j in range(i + 1, next_position):
                if nums[j] + j > nums[next_position] + next_position:
                    next_position = j
            i = next_position
        return steps
