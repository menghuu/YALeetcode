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
    def isMatch(self, s: str, p: str) -> bool:
        dps = [[False for _ in 'x' + p] for _ in 'x' + s]
        
        for i in range(len(dps)):
            for j in range(len(dps[0])):
                if i == 0 and j == 0:
                    dps[i][j] = True
                elif i == 0:
                    if p[j-1] == '*':
                        dps[i][j] = j-1 >= 0 and dps[i][j-1]
                elif j == 0:
                    dps[i][j] = False
                else:
                    ii = i - 1
                    jj = j - 1
                    sc = s[ii]
                    pc = p[jj]

                    if pc == '*':
                        if dps[i-1][j-1]:
                            dps[i][j] = True
                        if dps[i-1][j]:
                            dps[i][j] = ii - 1 >= 0 and s[ii-1] == s[ii] or dps[i][j]
                        if dps[i][j-1]:
                            dps[i][j] = True
                    elif pc == '?':
                        dps[i][j] = dps[i-1][j-1]
                    else:
                        dps[i][j] = dps[i-1][j-1] and pc == sc
            
        return dps[-1][-1]
