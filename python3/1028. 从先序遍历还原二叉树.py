#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
2020/06/18 每日一题
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def helper(s, bar):
            if not s:
                return None
            index = s.find(bar)
            if index == -1:
                root_value = int(s)
            else:
                root_value = int(s[:index])
            root = TreeNode(root_value)

            if index == -1:
                return root

            left_index = index + len(bar)
            while index != -1:
                index = s.find(bar, index + 1)
                if s[index + len(bar)] != '-' and s[index - 1] != '-':
                    break
            right_index = index
            if right_index == -1:
                root.left = helper(s[left_index:], bar + '-')
            else:
                root.left = helper(s[left_index: right_index], bar + '-')
                root.right = helper(s[right_index + len(bar):], bar + '-')

            return root

        return helper(S, '-')
