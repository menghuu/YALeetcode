#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianSortedArrays_log2(nums1, nums2)
        return self.findMedianSortedArrays_merge_sort1(nums1, nums2)
        return self.findMedianSortedArrays_merge_sort2(nums1, nums2)
    
    
    def findMedianSortedArrays_merge_sort(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        total_length = len(nums1) + len(nums2)
        while nums1 or nums2:
            if total_length // 2 + 1 == len(merged_nums):
                break
            if not nums1:
                merged_nums.append(nums2.pop(0))
            elif not nums2:
                merged_nums.append(nums1.pop(0))
            else:
                if nums1[0] <= nums2[0]:
                    merged_nums.append(nums1.pop(0))
                else:
                    merged_nums.append(nums2.pop(0))
        if total_length % 2 == 1:
            return merged_nums[-1]
        else:
            return (merged_nums[-1] + merged_nums[-2]) / 2

    def findMedianSortedArrays_merge_sort2(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        total_length = len(nums1) + len(nums2)
        while nums1 or nums2:
            if total_length // 2 + 1 == len(merged_nums):
                break
            if not nums1:
                index = total_length // 2 + 1 - len(merged_nums)
                tmp = nums2[:index]
                nums2 = nums2[index:]
                merged_nums.extend(tmp)
                break
            elif not nums2:
                index = total_length // 2 + 1 - len(merged_nums)
                tmp = nums1[:index]
                nums1 = nums1[index:]
                merged_nums.extend(tmp)
                break
            else:
                if nums1[0] <= nums2[0]:
                    merged_nums.append(nums1.pop(0))
                else:
                    merged_nums.append(nums2.pop(0))
        if total_length % 2 == 1:
            return merged_nums[-1]
        else:
            return (merged_nums[-1] + merged_nums[-2]) / 2
        
    def findMedianSortedArrays_log2(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        def get_k(start1, start2, k):
            if start1 == l1:
                return nums2[start2 + k - 1]
            elif start2 == l2:
                return nums1[start1 + k - 1]
            elif k == 1:
                return min(nums1[start1], nums2[start2])

            delta = min(l1 - start1, l2 - start2, k // 2)
            if nums1[start1 + delta - 1] <= nums2[start2 + delta - 1]:
                return get_k(start1 + delta, start2, k - delta)
            else:
                return get_k(start1, start2 + delta, k - delta)

        k1 = (l1 + l2 + 1) // 2
        k2 = (l1 + l2 + 2) // 2

        return (get_k(0, 0, k1) + get_k(0, 0, k2)) / 2
