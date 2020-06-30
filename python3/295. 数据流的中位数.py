#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
from heapq import heappushpop, heappush
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 小顶堆存放着较大那一部分的数字
        self.min_heap = []
        # 大顶堆存放着较小的那一部分的数字，并且得是取反的，因为实际上还是维护者小顶堆
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heappush(self.min_heap, num)
            return
        
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else:
            heappush(self.max_heap, -heappushpop(self.min_heap, num))
                

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
