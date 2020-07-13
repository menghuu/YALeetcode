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


def package01(nv, nw):
    for j in range(V, nv-1, -1):
        dps[j] = max(dps[j], dps[j - nv] + nw)

def packagefull(nv, nw):
    for j in range(nv, V + 1):
        dps[j] = max(dps[j], dps[j - nv] + nw)

for _ in range(N):
    
    v, w, s = list(map(int, sys.stdin.readline().strip().split()))
    
    if s == -1:
        package01(v, w)
    elif s == 0:
        packagefull(v, w)
    else:
        for k in range(s + 1):
            flag = False
            if 2 ** (k + 1) > s:
                ks = s - 2 ** k + 1
                flag = True
            else:
                ks = 2 ** k
            nv = ks * v
            nw = ks * w
            package01(nv, nw)
            if flag:
                break

print(dps[-1])
