#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
虽然这一道题目是leetcode的第一题，但是其会考虑面试者很多的细节讨论
包括
- 如果原始的nums中有重复的数字怎么办？那么直接使用dict(zip(nums, range(len(nums))))就不太合适了
- 如果[2,2], 4的情况，那么实际上返回[0, 1]是合理的，这个需要考虑到
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = set([i])
            else:
                d[num].add(i)
        for i in range(len(nums)):
            num = nums[i]
            num2 = target - num
            if num2 not in d:
                continue
            indexes = list(d[num2] - set([i]))
            if len(indexes) == 0:
                continue
            return [indexes[0], i]
