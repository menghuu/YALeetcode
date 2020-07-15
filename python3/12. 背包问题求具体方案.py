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

N, V = map(int, sys.stdin.readline().strip().split())

vs, ws = [], []
for _ in range(N):
    v, w = map(int, sys.stdin.readline().strip().split())
    vs.append(v)
    ws.append(w)

dps = [[0 for _ in range(V + 1)] for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    v, w = vs[i], ws[i]
    for j in range(V + 1):
        dps[i][j] = dps[i + 1][j]
        if j >= v:
            dps[i][j] = max(dps[i][j], dps[i + 1][j - v] + w)

vol = V
for i in range(N):
    ii = i + 1
    v, w = vs[i], ws[i]
    if dps[i][vol] == dps[i + 1][vol - v] + w:
        print(ii, end = ' ')
        vol -= v

