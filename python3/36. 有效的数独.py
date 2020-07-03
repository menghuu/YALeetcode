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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        visited = [set() for _ in range(27)]
        row_visited = [set() for _ in range(9)]
        column_visited = [set() for _ in range(9)]
        cell_visited = [[set() for _ in range(3)] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                bi, bj = i // 3, j // 3
                v = board[i][j]
                if v in row_visited[i] or v in column_visited[j] or v in cell_visited[bi][bj]:
                    return False
                else:
                    row_visited[i].add(v)
                    column_visited[j].add(v)
                    cell_visited[bi][bj].add(v)
        
        return True
