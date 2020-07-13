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
N = int(N)
V = int(V)

vs, ws, ss = [], [], []
vs2, ws2 = [], []

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    v, w, s = tuple(map(int, line.split()))
    vs.append(v)
    ws.append(w)
    ss.append(s)

    
# 最简单的做法，01背包的扩展
dps = [0 for _ in range(V + 1)]
for i, v, w, s in zip(range(N), vs, ws, ss):
    for j in range(V, -1, -1):
        # 为什么是从大到小，因为：个数是有限的，应该和01背包更像
        k = 1
        while k <= s and j - k * v >= 0:
            dps[j] = max(dps[j], dps[j - k * v] + k * w)
            k += 1
print(dps[-1])
