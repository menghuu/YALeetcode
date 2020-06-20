#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
有点难
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not s and not p:
            return True

        dps = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dps[0][0] = True

        for i in range(len(dps)):
            for j in range(len(dps[0])):

                if i == 0 and j == 0:
                    dps[i][j] = True
                elif i == 0:
                    if p[j - 1] == '*':
                        dps[i][j] = j - 2 >= 0 and dps[i][j - 2] or dps[i][j]
                    else:
                        dps[i][j] = False
                elif j == 0:
                    dps[i][j] = False
                else:
                    ii = i - 1
                    sc = s[ii]
                    jj = j - 1
                    pc = p[jj]
                    if pc == '*':
                        if dps[i - 1][j - 1]:
                            dps[i][j] = jj - 1 >= 0 and (p[jj - 1] == '.' or s[ii] == p[jj - 1]) or dps[i][j]
                        if dps[i - 1][j]:
                            dps[i][j] = jj - 1 >= 0 and (p[jj - 1] == '.' or s[ii] == p[jj - 1]) or dps[i][j]
                        if dps[i][j - 1]:
                            dps[i][j] = True
                        else:
                            dps[i][j] = j - 2 >= 0 and dps[i][j - 2] or dps[i][j]
                    elif pc == '.':
                        dps[i][j] = dps[i - 1][j - 1]
                    else:
                        dps[i][j] = dps[i - 1][j - 1] and pc == sc

        return dps[-1][-1]
