#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def pre_travel(node, ans):
            if not node:
                return
            ans.append(node.val)
            for child in node.children:
                pre_travel(child, ans)
        
        ans = []
        pre_travel(root, ans)
        return ans
