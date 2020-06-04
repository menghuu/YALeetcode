#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        if not slow:
            return False
        fast = slow.next
        if not fast:
            return False
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next 
            fast = fast.next.next
        return False
