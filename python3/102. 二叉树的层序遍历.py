#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        level = [root]
        while level:
            l = len(level)
            levels.append([one.val for one in level])
            for i in range(l):
                node = level[i]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            level = level[l:]
        return levels

