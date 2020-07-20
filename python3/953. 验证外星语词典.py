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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words = [word + '$' for word in words]
        char_vs_index = dict(zip(order, range(len(order))))
        char_vs_index['$'] = float('-inf')

        for i in range(len(words)-1):
            s1 = words[i]
            s2 = words[i + 1]

            # s1 <= s2
            for j in range(min(len(s1), len(s2))):
                c1 = s1[j]
                c2 = s2[j]
                if c1 == c2:
                    continue
                elif char_vs_index[c1] > char_vs_index[c2]:
                    return False
                else:
                    break
        return True
