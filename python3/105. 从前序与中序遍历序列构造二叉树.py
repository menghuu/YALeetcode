#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
虽然知道怎么做，但是写起来总是出问题
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pi, pj, ii, ij):
            if pi > pj or ii > ij:
                return None
            root_value = preorder[pi]
            index = inorder.index(root_value, ii, ij + 1)
            l = index - ii + 1
            root = TreeNode(root_value)
            root.left = build(pi+1, pi+l-1, ii, index-1)
            root.right = build(pi+l, pj, index+1, ij)
            return root
        root = build(0, len(preorder)-1, 0, len(inorder)-1)
        return root
