#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
这一题看上去很简单，但是前提是这个flap的逻辑是这样的，如果不是的话，似乎有点麻烦
可能会需要使用层次遍历来做
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def flap(node):
            if not node:
                return None
            right = flap(node.left)
            left = flap(node.right)
            node.left = left
            node.right = right
            return node
        
        return flap(root)

