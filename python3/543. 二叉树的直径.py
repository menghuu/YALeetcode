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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_leftmax_rightmax_totalmax(node):
            if not node:
                return None, None, None

            left_leftmax, left_rightmax, left_totalmax = get_leftmax_rightmax_totalmax(node.left)

            right_leftmax, right_rightmax, right_totalmax = get_leftmax_rightmax_totalmax(node.right)

            leftmax = 1
            if left_leftmax:
                leftmax = max(leftmax, left_leftmax + 1, left_rightmax + 1)
            
            rightmax = 1
            if right_leftmax:
                rightmax = max(rightmax, right_leftmax + 1, right_rightmax + 1)

            totalmax = max(1, leftmax + rightmax - 1, leftmax, rightmax)
            if left_totalmax:
                totalmax = max(totalmax, left_totalmax)
            if right_totalmax:
                totalmax = max(totalmax, right_totalmax)

            return leftmax, rightmax, totalmax

        _, _, totalmax = get_leftmax_rightmax_totalmax(root)
        
        if not totalmax:
            return 0
        else:
            return totalmax - 1
