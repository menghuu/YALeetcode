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
    def validPalindrome(self, s: str) -> bool:
        for left in range(len(s) // 2):
            right = len(s) - 1 - left
            if s[left] != s[right]:
                break

        if s[left] == s[right]:
            left += 1
            right -= 1

        if left >= right:
            return True

        def is_valid(s):
            for i in range(len(s) // 2):
                j = len(s) - 1 - i
                if s[i] != s[j]:
                    return False
            return True

        b1 = is_valid(s[left: right])
        b2 = is_valid(s[left+1: right+1])

        return b1 or b
