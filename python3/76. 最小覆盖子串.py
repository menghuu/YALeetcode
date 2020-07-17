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
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        char_vs_counts = Counter(t)
        window_char_counts = {}
        already = 0
        needed = len(char_vs_counts)
        ans = ''
        left, right = 0, 0

        while right < len(s):
            char = s[right]
            window_char_counts[char] = window_char_counts.get(char, 0) + 1
            if char in char_vs_counts and char_vs_counts[char] == window_char_counts[char]:
                already += 1
            
            while left <= right and already == needed:
                char = s[left]
                nans = s[left: right + 1]
                if not ans or len(nans) <= len(ans):
                    ans = nans
                if char in char_vs_counts and char_vs_counts[char] == window_char_counts[char]:
                    already -= 1
                window_char_counts[char] -= 1
                left += 1
            right += 1
        
        return ans

