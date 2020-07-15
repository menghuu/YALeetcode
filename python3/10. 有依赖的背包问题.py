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
c_indexes = [set() for _ in range(N)]
root_index = 0
for index in range(N):
    v, w, p = map(int, sys.stdin.readline().strip().split())
    vs.append(v)
    ws.append(w)
    if p != -1:
        c_indexes[p - 1].add(index)
    else:
        root_index = index

dps = [[0 for _ in range(V + 1)] for _ in range(N)]

def dfs(root_index):
    v, w = vs[root_index], ws[root_index]
    not_include_root_dps = [0 for _ in range(V + 1)]
    for index in c_indexes[root_index]:
        dfs(index)
        for j in range(V - v, -1, -1):
            for k in range(j + 1):
                not_include_root_dps[j] = max(not_include_root_dps[j], not_include_root_dps[j - k] + dps[index][k])
                
    for j in range(V, v - 1, -1):
        dps[root_index][j] = max(dps[root_index][j], not_include_root_dps[j - v] + w)
    for j in range(v):
        dps[root_index][j] = 0


dfs(root_index)

print(dps[root_index][-1])

