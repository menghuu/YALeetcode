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

N, V = sys.stdin.readline().strip().split()
N, V = int(N), int(V)

vs, ws = [], []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break 
    v, w = line.split()
    vs.append(int(v))
    ws.append(int(w))

dps = [0 for _ in range(V+1)]

for i, v, w in zip(range(N), vs, ws):
    for j in range(V, -1, -1):
        jj = j - v
        if jj >= 0:
            dps[j] = max(dps[j], dps[jj] + w)

print(dps[-1])
