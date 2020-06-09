#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = [root]
        while level:
            l = len(level)
            levels.append([node.val for node in level])
            for i in range(l):
                node = level[i]
                for child in node.children:
                    if child:
                        level.append(child)
            level = level[l:]
        return levels
