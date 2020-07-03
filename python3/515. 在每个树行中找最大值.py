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
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            l = len(level)
            m = float('-inf')
            for i in range(l):
                root = level[i]
                m = max(root.val, m)
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            level = level[l:]
            ans.append(m)
        return ans

