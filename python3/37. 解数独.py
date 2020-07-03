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
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row_visited = [set() for _ in range(9)]
        column_visited = [set() for _ in range(9)]
        box_visited = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                if v == '.':
                    continue
                bi, bj = i // 3, j // 3
                row_visited[i].add(v)
                column_visited[j].add(v)
                box_visited[bi][bj].add(v)

        def set_state(i, j, v):
            bi, bj = i // 3, j // 3
            board[i][j] = v
            row_visited[i].add(v)
            column_visited[j].add(v)
            box_visited[bi][bj].add(v)

        def reset_state(i, j, v):
            bi, bj = i // 3, j // 3
            board[i][j] = '.'
            row_visited[i].remove(v)
            column_visited[j].remove(v)
            box_visited[bi][bj].remove(v)

        all_availables = set([str(i) for i in range(1, 10)])

        def bfs(i, j):
            if i == 9:
                return True
            bi, bj = i // 3, j // 3
            if board[i][j] == '.':
                for v in all_availables:
                    if v in row_visited[i] or v in column_visited[j] or v in box_visited[bi][bj]:
                        continue
                    else:
                        set_state(i, j, v)
                        if bfs(i + (j + 1) // 9, (j + 1) % 9):
                            return True
                        reset_state(i, j, v)
            else:
                return bfs(i + (j + 1) // 9, (j + 1) % 9)
            return False

        flag = bfs(0, 0)
        return flag
