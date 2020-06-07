#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
这一题就没有像https://leetcode-cn.com/problems/trapping-rain-water/ 接雨水那一题中
那样在取index0时做判断stack是否是空
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                index0 = stack[-1]
                w = i - index0 - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans
