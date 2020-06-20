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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        current = head 
        while l1 or l2:
            if l1 and l2:
                v = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                v = l1.val + carry
                l1 = l1.next
            else:
                v = l2.val + carry
                l2 = l2.next
            v, carry = v % 10, v // 10
            node = ListNode(v)
            current.next = node
            current = node
            
        if carry:
            current.next = ListNode(carry)
        
        return head.next
