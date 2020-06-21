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
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        ans = 0
        gg = list(sorted(g))
        ss = list(sorted(s))

        sindex = 0
        gindex = 0
        while sindex < len(ss) and gindex < len(gg):
            if ss[sindex] >= gg[gindex]:
                ans += 1
                sindex += 1
                gindex += 1
            else:
                sindex += 1
        return ans
