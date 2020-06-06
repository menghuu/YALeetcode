#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
这里最有意思的是最后面的那个index > j 的操作以及  index = d.get(n3. i)的操作，值得细细品味
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = list(sorted(nums))
        def qsort(nums, start_index, end_index):
            if start_index >= end_index:
                return
            povit = nums[start_index]
            i = start_index
            j = end_index
            while i < j:
                while i < j and nums[j] > povit:
                    j -= 1
                while i < j and nums[i] <= povit:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[start_index], nums[i] = nums[i], nums[start_index]
            qsort(nums, start_index, i - 1)
            qsort(nums, i + 1, end_index)
        qsort(nums, 0, len(nums) - 1)
        d = dict(zip(nums, range(len(nums))))
        ans = []
        for i in range(len(nums)):
            n1 = nums[i]
            if i != 0 and nums[i - 1] == n1:
                continue
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                if j != i + 1 and nums[j - 1] == n2:
                    continue
                n3 = 0 - n1 - n2
                index = d.get(n3, i)
                if index > j:
                    ans.append([n1, n2, n3])
        return ans
        
                

