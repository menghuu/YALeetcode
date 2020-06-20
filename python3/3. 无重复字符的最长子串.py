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
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_vs_index = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            c = s[right]
            if char_vs_index.get(c, -1) >= left:
                left = char_vs_index[c] + 1
            
            char_vs_index[c] = right
            ans = max(right - left + 1, ans)
        
        return ans
