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
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dps = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dps[i][j] = 0
                elif i == 0 and j == 0:
                    dps[i][j] = 1
                elif i == 0:
                    dps[i][j] = dps[i][j-1]
                elif j == 0:
                    dps[i][j] = dps[i-1][j]
                else:
                    dps[i][j] = dps[i-1][j] + dps[i][j-1]
        return dps[-1][-1]
