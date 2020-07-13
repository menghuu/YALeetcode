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
    
    for k in range(s):
        kk = 2 ** k
        if kk > s:
            if vs2:
                vs2.pop()
                ws2.pop()
            kk = s - kk // 2 + 1
            vs2.append(kk * v)
            ws2.append(kk * w)
            break
        else:
            vs2.append(kk * v)
            ws2.append(kk * w)

    
assert N == len(vs)

# 最简单的做法，01背包的扩展
dps = [0 for _ in range(V + 1)]
for i, v, w, s in zip(range(N), vs, ws, ss):
    for j in range(V, -1, -1):
        # 为什么是从大到小，因为：个数是有限的，应该和01背包更像
        k = 1
        while k <= s and j - k * v >= 0:
            dps[j] = max(dps[j], dps[j - k * v] + k * w)
            k += 1
# print(dps[-1])

# 二进制优化，优化点在k的选择上，在上面需要重复s次（大概），但是实际上可以继续减少这个尝试的次数
dps = [0 for _ in range(V + 1)]
for i, v, w in zip(range(len(vs2)), vs2, ws2):
    for j in range(V, -1, -1):
        if j - v >= 0:
            dps[j] = max(dps[j], dps[j - v] + w)
# print(dps[-1])


# O(V*N)版本的解法，这是最优的解法， 略过吧，有点复杂啊


