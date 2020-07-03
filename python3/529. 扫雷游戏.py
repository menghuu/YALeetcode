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
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []
        
        def bfs(i, j):
            if board[i][j] =='X':
                return True
            elif board[i][j] in ['1', 'B']:
                return 
            # board[i][j] == 'E'

            meet_m = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                        meet_m += 1
            if meet_m:
                board[i][j] = str(meet_m)
            else:
                board[i][j] = 'B'
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n:
                            bfs(ni, nj)
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        bfs(click[0], click[1])

        return board

