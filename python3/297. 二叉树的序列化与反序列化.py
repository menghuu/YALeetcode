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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        levels = []
        level = [root]
        while level:
            l = len(level)
            levels.append(','.join(str(one.val) if one is not None else 'null' for one in level))
            for i in range(l):
                node = level[i]
                if not node:
                    continue
                level.append(node.left)
                level.append(node.right)
            level = level[l:]
        levels = levels[:-1]
        return '[' + (','.join(levels)) + ']'

    def deserialize_inner(self, nums):
        root = TreeNode(nums.pop(0))
        level = [root]

        while nums:
            node = level.pop(0)

            lval = nums.pop(0)
            rval = nums.pop(0)

            if lval is None:
                node.left = None
            else:
                node.left = TreeNode(lval)
            if rval is None:
                node.right = None
            else:
                node.right = TreeNode(rval)

            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nums = [
            int(one) if one != 'null' else None
            for one in data[1:-1].split(',')
        ]

        return self.deserialize_inner(nums)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
