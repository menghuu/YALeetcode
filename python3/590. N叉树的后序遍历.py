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
    def postorder(self, root: 'Node') -> List[int]:
        def post_travel(node, ans):
            if not node:
                return 
            
            for child in node.children:
                post_travel(child, ans)
            
            ans.append(node.val)
        ans = []
        post_travel(root, ans)
        return ans
