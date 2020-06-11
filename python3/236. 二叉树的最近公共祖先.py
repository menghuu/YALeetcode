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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.p_path = []
        self.q_path = []
        def find_node(path, node, to_found, record_path):
            path.append(node)

            if node == to_found:
                record_path.extend(path)
            if node.left:
                find_node(path, node.left, to_found, record_path)
            if node.right:
                find_node(path, node.right, to_found, record_path)
            
            path.pop()
        
        find_node([], root, p, self.p_path)
        find_node([], root, q, self.q_path)
        
        while self.p_path and self.q_path and self.p_path[0] == self.q_path[0]:
            a, b = self.p_path.pop(0), self.q_path.pop(0)

        return a

