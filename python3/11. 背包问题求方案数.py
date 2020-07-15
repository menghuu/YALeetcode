#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
import sys, math

mod = 10 ** 9 + 7

# 这里面虽然写成了INF，但是实际上并不能真的是float('inf')或者准确来说不能是float('-inf')
INF = 1000000

N, V = map(int, sys.stdin.readline().strip().split())

dps = [-INF for _ in range(V + 1)]
counts = [0 for _ in range(V + 1)]
counts[0] = 1

for _ in range(N):
    v, w = map(int, sys.stdin.readline().strip().split())
    
    for j in range(V, v - 1, -1):
        ndp = dps[j - v] + w
        if ndp == dps[j]:
            counts[j] += counts[j - v]
        elif ndp > dps[j]:
            dps[j] = ndp
            counts[j] = counts[j - v]

ans = 0
m = max(dps)
for dp, c in zip(dps, counts):
    if dp == m:
        ans += c
print(ans % mod)
