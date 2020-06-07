#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
42. Trapping Rain Water
个人感觉能写出动态规划的做法或者双指针的做法都还行，使用栈的可能需要详细记一下
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        return self.using_stack(height)
        return self.using_2points(height)
        return self.using_dps(height)

    def using_stack(self, height):
        height = height
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                h0 = height[stack.pop()]
                if not stack:
                    break
                pindex = stack[-1]
                w = i - pindex - 1
                h = min(height[i], height[pindex]) - h0
                ans += w * h
            stack.append(i)
        return ans

    def using_2points(self, height):
        if not height:
            return 0
        lmax = height[0]
        rmax = height[-1]
        lindex = 0
        rindex = len(height) - 1

        ans = 0
        while lindex <= rindex:
            if height[lindex] < height[rindex]:
                h = height[lindex]
                lmax = max(lmax, h)
                ans += lmax - h
                lindex += 1
            else:
                h = height[rindex]
                rmax = max(rmax, h)
                ans += rmax - h
                rindex -= 1
        return ans

    def using_dps(self, height):
        dps1 = [0]
        dps2 = [0]
        for h in height[:-1]:
            dps1.append(max(h, dps1[-1]))
        for h in height[::-1][:-1]:
            dps2.append(max(h, dps2[-1]))
        dps2 = dps2[::-1]
        
        ans = 0
        for i in range(len(height)):
            ans += max(height[i], min(dps1[i], dps2[i])) - height[i]
        return ans
