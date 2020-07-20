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
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, visited, word):
            if not word:
                return True
            elif word[0] != board[i][j]:
                return False
            else:
                # word is not empty and word[0] == board[i][j]
                if len(word) == 1:
                    return True
                visited[i][j] = True
                for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < len(board) and 0 <= jj < len(board[ii]) and not visited[ii][jj] and backtrack(ii, jj, visited, word[1:]):
                        return True
                visited[i][j] = False
                return False
            
        visited = [[False for _ in board[0]] for _ in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                flag = backtrack(i, j, visited, word)
                if flag:
                    return True
        return False
