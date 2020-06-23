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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = list(sorted(intervals, key=lambda l: l[0]))

        ans = [intervals[0]]
        for t in intervals:
            if t[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], t[1])
            else:
                ans.append(t)
        return ans
