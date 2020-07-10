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
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dps[i][j] 表示i个0， j个1能有最多多少个字符串能够表达出来
        # m个0， n个1
        # i,    j
        dps = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # （m+1) * (n+1)

        from collections import Counter

        for str in strs[:]:
            counter = Counter(str)
            one_counts = counter.get('1', 0)
            zero_counts = counter.get('0', 0)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    ii = i - zero_counts
                    jj = j - one_counts
                    if ii >= 0 and jj >= 0:
                        dps[i][j] = max(dps[i][j], dps[ii][jj] + 1)

        return dps[-1][-1]
