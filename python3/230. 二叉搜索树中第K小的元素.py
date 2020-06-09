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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def pre_order(node, path):
            if node.left:
                pre_order(node.left, path)
            path.append(node)
            if node.right:
                pre_order(node.right, path)
        
        path = []
        pre_order(root, path)

        return path[k-1].val
