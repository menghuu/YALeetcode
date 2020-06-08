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
    def isValidBST(self, root: TreeNode) -> bool:
        def get_max_min(node):

            if not node.left and not node.right:
                return node.val, node.val, True
            
            if node.left:
                leftmax, leftmin, b = get_max_min(node.left)
                if not b:
                    return leftmax, leftmin, b
            
            if node.right:
                rightmax, rightmin, b = get_max_min(node.right)
                if not b:
                    return rightmax, rightmin, b
            
            if not node.left:
                return max(node.val, rightmax), min(node.val, rightmin), node.val < rightmin
            
            if not node.right:
                return max(node.val, leftmax), min(node.val, leftmin), node.val > leftmax
            
            return rightmax, leftmin, node.val < rightmin and node.val > leftmax

        if not root:
            return True
            
        _, _, b = get_max_min(root)
        return b
        

