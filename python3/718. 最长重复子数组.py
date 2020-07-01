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
    def findLength(self, A: List[int], B: List[int]) -> int:

        dps = [[0 for _ in B] for _ in A]

        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if i == 0 or j == 0:
                    dps[i][j] = int(A[i] == B[j])
                elif A[i] == B[j]:
                    dps[i][j] = dps[i-1][j-1] + 1
                else:
                    dps[i][j] = 0
                ans = max(ans, dps[i][j])

        return ans

