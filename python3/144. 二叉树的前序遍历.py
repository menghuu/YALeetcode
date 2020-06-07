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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def pre_travel(node, ans):
            if not node:
                return
            ans.append(node.val)
            pre_travel(node.left, ans)
            pre_travel(node.right, ans)
        ans = []
        pre_travel(root, ans)
        return ans
