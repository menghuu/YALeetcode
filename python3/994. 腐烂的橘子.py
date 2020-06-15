#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
from typing import List, Tuple
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(start_positions: List[Tuple[int, int]], steps, grid):
            if len(start_positions) == 0:
                return steps
            next_positions = []
            for x, y in start_positions:
                new_xy = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1)
                ]
                for new_x, new_y in new_xy:
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) \
                            and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        next_positions.append((new_x, new_y))
            return bfs(next_positions, steps + 1, grid)

        start_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    start_positions.append((i, j))
        steps = bfs(start_positions, -1, grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(0, steps)
