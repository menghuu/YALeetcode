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
    def countSubstrings(self, s: str) -> int:
        # dps[i][j] 表示 s[i: j + 1]是否是一个回文子串
        dps = [[False for _ in s] for _ in s]
        dps[-1][-1] = True

        ans = 1
        for i in range(len(s) - 2, -1, -1):
            dps[i][i] = True
            ans += 1
            if s[i] == s[i + 1]:
                dps[i][i + 1] = True
                ans += 1
            else:
                dps[i][i + 1] = False
            for j in range(i + 2, len(s)):
                if dps[i + 1][j - 1] and s[i] == s[j]:
                    dps[i][j] = True
                    ans += 1
                else:
                    dps[i][j] = False

        return ans
