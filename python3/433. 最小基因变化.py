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
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if len(start) != len(end) or end not in bank:
            return -1
        
        bank = set(bank)
        #bank.remove(end)

        from collections import defaultdict
        pattern_vs_strings = defaultdict(set)

        for b in bank:
            for i in range(len(b)):
                p = b[:i] + '*' + b[i+1:]
                pattern_vs_strings[p].add(b)
        
        visited = set()
        
        self.ans = float('inf')

        def bfs(start, end, times):
            if start == end:
                return times
            visited.add(start)
            for i in range(len(start)):
                p = start[:i] + '*' + start[i+1:]
                for b in pattern_vs_strings[p]:
                    if b not in visited:
                        self.ans = min(self.ans, bfs(b, end, times+1))
            return self.ans
        
        bfs(start, end, 0)

        import math

        return -1 if math.isinf(self.ans) else self.ans
