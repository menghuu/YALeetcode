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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, paths, nums):
            paths.append(path[:])

            for i in range(len(nums)):
                num = nums[i]
                path.append(num)
                backtrack(path, paths, nums[i+1:])
                path.pop()
        
        path = []
        paths = []
        backtrack(path, paths, nums)
        return paths
