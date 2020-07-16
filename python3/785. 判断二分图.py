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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        WHITE = 0
        RED = 1
        GREEN = 2

        colors = [WHITE for _ in graph]

        def bfs(parent_color, current_index):
            if colors[current_index] == parent_color:
                return False
            elif colors[current_index] == WHITE:
                colors[current_index] = 3 - parent_color
                for cindex in graph[current_index]:
                    flag = bfs(colors[current_index], cindex)
                    if not flag:
                        return False
            else:
                pass
            return True

        for i in range(len(graph)):
            if colors[i] == WHITE:
                flag = bfs(GREEN, i)
                if not flag:
                    return flag
        return True

