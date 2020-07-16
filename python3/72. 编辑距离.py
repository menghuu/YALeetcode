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
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = ' ' + word1
        word2 = ' ' + word2
        dps = [[None for _ in word2] for _ in word1]

        for i in range(len(word1)):
            dps[i][0] = i
        for j in range(len(word2)):
            dps[0][j] = j

        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                lu = dps[i - 1][j - 1]
                if word1[i] == word2[j]:
                    dps[i][j] = lu
                else:
                    l = dps[i][j - 1]
                    u = dps[i - 1][j]
                    m = min(lu, l, u)

                    if m == lu:
                        # 修改这个字符
                        dps[i][j] = lu + 1
                    elif m == l:
                        # 插入word2[j - 1]这个字符
                        dps[i][j] = l + 1
                    else:
                        # 将word2[j - 1]这个字符删除掉与word1[:i]匹配上
                        dps[i][j] = u + 1
        
        return dps[-1][-1]


