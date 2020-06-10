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
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dps = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dps[i][j] = grid[i][j]
                if i == 0 and j == 0:
                    ...
                elif i == 0:
                    dps[i][j] += dps[i][j-1]
                elif j == 0:
                    dps[i][j] += dps[i-1][j]
                else:
                    dps[i][j] += min(dps[i-1][j], dps[i][j-1])
        
        return dps[-1][-1]
