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
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s:
            return 0
        if s[0] == '-':
            positive = False
            MAX = 2 ** 31
            s = s[1:]
        else:
            positive = True
            MAX = 2 ** 31 - 1
            if s[0] == '+':
                s = s[1:]

        ans = 0
        for c in s:
            if not ord('0') <= ord(c) <= ord('9'):
                break
            if MAX // 10 < ans:
                return MAX if positive else -MAX
            ans *= 10
            n = int(c)
            if MAX - ans < n:
                return MAX if positive else -MAX
            ans += n

        return ans if positive else -ans
