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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dps = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                c = matrix[i][j]
                if i == 0 or j == 0:
                    dps[i][j] = int(c == '1')
                elif c == '0':
                    dps[i][j] = 0
                else:
                    lul = dps[i - 1][j - 1]
                    ll = dps[i][j - 1]
                    ul = dps[i - 1][j]
                    
                    ml = min(lul, ll, ul) + 1

                    dps[i][j] = ml
                ans = max(ans, dps[i][j])

        return ans * ans

