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
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_i, start_j = 0, 0
        end_i, end_j = 0, 0

        self.v_counts = 0
        visited = [[False for _ in grid[0]] for _ in grid]
        total_v_counts = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                n = grid[i][j]
                total_v_counts += 1
                if n == 1:
                    start_i, start_j = i, j
                elif n == 2:
                    end_i, end_j = i, j
                elif n == -1:
                    visited[i][j] = True
                    self.v_counts += 1
                else:
                    visited[i][j] = False

        self.path_counts = 0


        def backtrack(i, j, visited):
            visited[i][j] = True
            self.v_counts += 1

            if i == end_i and j == end_j:
                self.path_counts += int(self.v_counts == total_v_counts)
            else:
                for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[ii]) and not visited[ii][jj]:
                        backtrack(ii, jj, visited)

            visited[i][j] = False
            self.v_counts -= 1


        backtrack(start_i, start_j, visited)

        return self.path_counts
