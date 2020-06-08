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
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        def backtrack(node, depth):
            if not node:
                self.depth = max(depth, self.depth)
                return
            
            backtrack(node.left, depth + 1)
            backtrack(node.right, depth + 1)
        
        backtrack(root, 0)
        return self.depth

