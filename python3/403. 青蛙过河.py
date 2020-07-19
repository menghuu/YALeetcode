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
    def canCross(self, stones: List[int]) -> bool:
        dps = [set() for _ in stones]
        for i in range(len(stones)):
            delta = stones[-1] - stones[i]
            dps[-1].add(delta)
            dps[-1].add(delta - 1)
            dps[-1].add(delta + 1)

        for i in range(len(stones) - 2, -1, -1):
            for j in range(i, len(stones)):
                delta = stones[j] - stones[i]
                if delta - 1 in dps[j] or delta in dps[j] or delta + 1 in dps[j]:
                    dps[i].add(delta)

        return 1 in dps[0]
