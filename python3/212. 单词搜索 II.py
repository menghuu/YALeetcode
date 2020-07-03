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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_dict = {}
        for word in words:
            _dict = trie_dict
            for c in word:
                if c not in _dict:
                    _dict[c] = {}
                _dict = _dict[c]
            _dict[-1] = True
        
        m = len(board)
        n = len(board[0])

        visited = set()
        ans = set()
        def bfs(i, j, _dict, path):
            c = board[i][j]
            
            if c not in _dict:
                return False

            path.append(c)
            visited.add((i,j))

            if -1 in _dict[c]:
                ans.add(''.join(path))

            for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if (ni, nj) not in visited and 0 <= ni < m and 0 <= nj < n:
                    bfs(ni, nj, _dict[c], path)

            visited.remove((i,j))
            path.pop()
        
        for i in range(m):
            for j in range(n):
                bfs(i, j, trie_dict, [])
        
        return list(ans)

