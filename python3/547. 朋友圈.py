#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        return self.findCircleNum_disjoin_set(M)

        visited = set()

        n = len(M)

        def bfs(i):
            visited.add(i)
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    bfs(j)

        ans = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                ans += 1
        
        return ans
    
    def findCircleNum_disjoin_set(self, M):
        n = len(M)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find_root(i):
            if parent[i] != i:
                return find_root(parent[i])
            else:
                return i
        
        def union(i, j):
            iroot = find_root(i)
            jroot = find_root(j)
            
            if iroot == jroot:
                return
            elif rank[iroot] > rank[jroot]:
                parent[jroot] = iroot
            elif rank[iroot] < rank[jroot]:
                parent[iroot] = jroot
            else:
                parent[iroot] = jroot
                rank[jroot] += 1
        
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    union(i, j)
        for i in range(n):
            parent[i] = find_root(parent[i])
        
        return len(set(parent))
