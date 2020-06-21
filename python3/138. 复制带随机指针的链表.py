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
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        current = head
        while current:
            node = Node(current.val, current.next)
            current.next = node
            current = node.next
        
        current = head
        while current:
            if current.random:
                random = current.random.next
            else:
                random = None
            current.next.random = random
            current = current.next.next
        
        current = head.next
        while current.next:
            current.next = current.next.next
            current = current.next
        return head.next


