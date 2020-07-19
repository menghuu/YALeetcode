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
    def longestPalindrome(self, s: str) -> str:
        def expand(s, i, j):
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]
        
        ans = ''
        for i in range(len(s)):
            ans1 = expand(s, i, i)
            ans2 = expand(s, i, i + 1)
            if len(ans1) > len(ans):
                ans = ans1
            if len(ans2) > len(ans):
                ans = ans2
        return ans
