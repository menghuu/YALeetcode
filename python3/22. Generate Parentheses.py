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
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, paths, left, right):
            if left == right == n:
                paths.append(''.join(path))
                return
            
            if left < n:
                path.append('(')
                backtrack(path, paths, left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(path, paths, left, right + 1)
                path.pop()
        
        path = []
        paths = []
        backtrack(path, paths, 0, 0)
        return paths
