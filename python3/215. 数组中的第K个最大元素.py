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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappushpop, heappop
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            elif heap[0] < num:
                heappushpop(heap, num)
        return heappop(heap)
