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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isvalid(s, t):
            if not s and not t:
                return True
            elif s and t:
                if s.val != t.val:
                    return False
                else:
                    if isvalid(s.left, t.left) and isvalid(s.right, t.right):
                        return True
                    else:
                        return False
            else:
                return False
            
        def preorder(s, t):
            if s.val == t.val and isvalid(s, t):
                return True
            if s.left:
                if preorder(s.left, t):
                    return True
            if s.right:
                if preorder(s.right, t):
                    return True
            return False
        
        ans = preorder(s, t)
        return ans
