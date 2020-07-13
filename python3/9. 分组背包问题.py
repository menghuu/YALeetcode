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

N, V = list(map(int, sys.stdin.readline().strip().split()))

dps = [0 for _ in range(V + 1)]

for _ in range(N):
    s = int(sys.stdin.readline().strip())
    ndps = dps[:]
    for _ in range(s):
        v, w = map(int, sys.stdin.readline().strip().split())
        for j in range(V, v-1, -1):
            ndps[j] = max(ndps[j], dps[j - v] + w)
    dps = ndps

print(dps[-1])
