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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dps = [False for _ in range(len(s) + 1)]
        dps[0] = True
        for right in range(len(s)):
            for left in range(right + 1):
                sub = s[left: right + 1]
                if dps[left] and sub in wordDict:
                    dps[right + 1] = True
                    break
        return dps[-1]
