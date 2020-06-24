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
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        word_counts = defaultdict(int)
        word = ''

        ai = ord('a')
        zi = ord('z')
        Ai = ord('A')
        Zi = ord('Z')
        for c in paragraph + '.':
            ci = ord(c)
            if ai <= ci <= zi:
                word += c
            elif Ai <= ci <= Zi:
                word += c.lower()
            else:
                if word not in banned + ['']:
                    word_counts[word] += 1
                word = ''

        word = ''
        count = 0
        for w, c in word_counts.items():
            if c >= count:
                word = w
                count = c
        return word
