#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
import sys

N, V, M = list(map(int, sys.stdin.readline().strip().split()))

dps = [[0 for _ in range(M + 1)] for _ in range(V + 1)]

for _ in range(N):
    v, m, w = list(map(int, sys.stdin.readline().strip().split()))
    
    # 01背包
    for i in range(V, v - 1, -1):
        for j in range(M, m - 1, -1):
            dps[i][j] = max(dps[i][j], dps[i - v][j - m] + w)

print(dps[-1][-1])
