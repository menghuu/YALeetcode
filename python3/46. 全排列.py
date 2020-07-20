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
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, paths, nums):
            if not nums:
                paths.append(path[:])
            else:
                for i in range(len(nums)):
                    path.append(nums[i])
                    backtrack(path, paths, nums[:i] + nums[i+1:])
                    path.pop()
        
        path = []
        paths = []
        backtrack(path, paths, nums)
        return paths
