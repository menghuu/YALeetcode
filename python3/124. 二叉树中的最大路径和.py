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
    def maxPathSum(self, root: TreeNode) -> int:
        
        def get_leftmax_rightmax_totalmax(node):
            if not node:
                return None, None, None
            
            left_leftmax, left_rightmax, left_totalmax = get_leftmax_rightmax_totalmax(node.left)

            right_leftmax, right_rightmax, right_totalmax = get_leftmax_rightmax_totalmax(node.right)

            if left_leftmax is None:
                leftmax = node.val
            else:
                leftmax = max(left_leftmax, left_rightmax, 0) + node.val
            
            if right_leftmax is None:
                rightmax = node.val
            else:
                rightmax = max(right_leftmax, right_rightmax, 0) + node.val

            totalmax = max(node.val, leftmax + rightmax - node.val)
            if left_totalmax is not None:
                totalmax = max(totalmax, left_totalmax)
            if right_totalmax is not None:
                totalmax = max(totalmax, right_totalmax)

            return leftmax, rightmax, totalmax
            
        
        _, _, totalmax = get_leftmax_rightmax_totalmax(root)
        
        return totalmax
