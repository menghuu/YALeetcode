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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head
        left = prehead
        right = prehead
        gap = 0
        while right.next:
            right = right.next
            if gap == n:
                left = left.next
            else:
                gap += 1
        
        left.next = left.next.next

        return prehead.next
