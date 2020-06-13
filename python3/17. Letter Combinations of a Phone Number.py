#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
典型的回溯算法
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(path, paths, s):
            if not s:
                paths.append(''.join(path))
                return

            n = s[0]
            s = s[1:]
            for c in d[n]: 
                path.append(c)
                backtrack(path, paths, s)
                path.pop()
        path = []
        paths = []
        s = digits
        if not s:
            return paths
        backtrack(path, paths, s)
        return paths
