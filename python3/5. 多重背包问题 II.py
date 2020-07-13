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

vs, ws, ss = [], [], []

dps = [0 for _ in range(V + 1)]

for _ in range(N):
    
    v, w, s = list(map(int, sys.stdin.readline().strip().split()))
    
    for k in range(s + 1):
        flag = False
        if 2 ** (k + 1) > s:
            nk = s - 2 ** k + 1
            flag = True
        else:
            nk = 2 ** k
        nv = nk * v
        nw = nk * w
        
        for j in range(V, nv - 1, -1):
            dps[j] = max(dps[j], dps[j - nv] + nw)
        
        if flag:
            break
        
print(dps[-1])
