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

# dps[j]
dps = [0 for _ in range(V + 1)]

# dps[i][j]

for _ in range(N):
    v, w = map(int, sys.stdin.readline().strip().split())
    
    for j in range(V, v - 1, -1):
        dps[j] = max(dps[j], dps[j - v] + w)

print(dps[-1])
