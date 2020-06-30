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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        else:
            n = len(board[0])

        def bfs(board, i, j):
            assert board[i][j] == 'O'

            board[i][j] = '#'
            deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in deltas:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                    bfs(board, ni, nj)

        for i in range(m):
            if board[i][0] == 'O':
                bfs(board, i, 0)
            if board[i][n - 1] == 'O':
                bfs(board, i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                bfs(board, 0, j)
            if board[m - 1][j] == 'O':
                bfs(board, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        

