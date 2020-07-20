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
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy
        def backtrack(boards, board, row, columns: set, xy_diff: List[int], xy_sum: List[int]):
            if row == len(board):
                boards.append([''.join(row) for row in board])
            for col in columns:
                if xy_diff[row - col] and xy_sum[row + col]:
                    board[row][col] = 'Q'
                    xy_diff[row - col] = False
                    xy_sum[row + col] = False

                    backtrack(boards, board, row + 1, columns.difference({col}), xy_diff, xy_sum)

                    xy_diff[row - col] = True
                    xy_sum[row + col] = True
                    board[row][col] = '.'
        boards = []
        board = [list('.' * n) for _ in range(n)]
        columns = set(range(n))
        xy_diff = [True for _ in range(2 * n - 1)]
        xy_sum = [True for _ in range(2 * n - 1)]
        backtrack(boards, board, 0, columns, xy_diff, xy_sum)
        return boards
