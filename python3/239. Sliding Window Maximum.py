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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return self.using_queue(nums, k)
        l = len(nums)
        leftmaxs = [0] * l
        leftmaxs[0] = nums[0]
        rightmaxs = [0] * l
        rightmaxs[l-1] = nums[l-1]
        for i in range(1, len(nums)):
            if i % k == 0:
                leftmaxs[i] = nums[i]
            else:
                leftmaxs[i] = max(nums[i], leftmaxs[i-1])
            j = l - i - 1
            if (j + 1) % k == 0: # 这里的判断条件十分神奇，仔细想想才能知道为啥
                rightmaxs[j] = nums[j]
            else:
                rightmaxs[j] = max(nums[j], rightmaxs[j+1])
        ans = []
        for i in range(k - 1, len(nums)):
            j = i - k + 1
            ans.append(max(leftmaxs[i], rightmaxs[j]))
        return ans
    
    def using_queue(self, nums, k):
        from queue import deque
        queue = deque()
        ans = []
        for i in range(len(nums)):
            while queue and i - queue[0] + 1 > k:
                # 这个是说边界不满足k的条件了
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                # 这个是要保持这个栈（如果看成栈的话）是顶小下大的
                queue.pop()
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans[k-1:]
