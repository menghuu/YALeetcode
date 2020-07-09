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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        def siftdown(heap, index, length=None):
            if length is None:
                length = len(heap)

            if index >= length:
                return
            min_index = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < length and heap[min_index] > heap[left_index]:
                min_index = left_index
            if right_index < length and heap[min_index] > heap[right_index]:
                min_index = right_index
            if min_index != index:
                heap[index], heap[min_index] = heap[min_index], heap[index]
                siftdown(heap, min_index, length)
        
        def heapify(heap):
            last_index = len(heap) - 1
            last_parent_index = (last_index - 1) // 2
            for index in range(last_parent_index, -1, -1):
                siftdown(heap, index)

        from collections import Counter

        heap = [(-count, word) for word, count in Counter(words).items()]

        heapify(heap)

        ans = []
        for _ in range(k):
            heap[0], heap[-1] = heap[-1], heap[0]

            ans.append(heap[-1][1])

            heap.pop()
            siftdown(heap, 0)      

        return ans
