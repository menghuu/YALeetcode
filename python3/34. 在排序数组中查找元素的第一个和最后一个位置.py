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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(nums, i, j, target):
            if i > j:
                return -1
            m = (i + j) // 2
            num = nums[m]
            if num == target:
                return m
            elif num < target:
                return find(nums, m+1, j, target)
            else:
                return find(nums, i, m-1, target)
        
        index = find(nums, 0, len(nums)-1, target)

        if index == -1:
            return [-1, -1]

        i = index        
        while True:
            ii = find(nums, 0, i-1, target)
            if ii == -1:
                break
            else:
                i = ii
        
        j = index
        while True:
            jj = find(nums, j+1, len(nums)-1, target)
            if jj == -1:
                break
            else:
                j = jj
        return [i, j]

