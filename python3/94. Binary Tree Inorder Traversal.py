#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
中序遍历是指：子树的根节点在什么顺序上被访问到，中序就是中间被访问到，先序就是最靠前，后续就是最靠后
迭代方法看看就好，实际上不是很好想
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        ### 迭代
        stack = []
        res = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            res.append(node.val)
            current = node.right
        return res

        ### 迭代
        def helper(node, res):
            if node.left:
                helper(node.left, res)
            res.append(node.val)
            if node.right:
                helper(node.right, res)
        
        res = []
        if not root:
            return res
        else:
            helper(root, res)
            return res
