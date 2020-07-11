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

for v, w in zip(vs, ws):
    for i in range(V, -1, -1):
        ii = i - v
        if ii >= 0:
            dps[i] = max(dps[i], dps[ii] + w)

print(dps[-1])
