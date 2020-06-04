#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
其实这里是做了一个pre_head的操作，这也是为什么head2 要是fast.next
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        if not slow:
            return None
        fast = slow.next
        if not fast:
            return None
        is_cycle = False
        while fast and fast.next:
            if fast == slow:
                is_cycle = True
                break
            slow = slow.next 
            fast = fast.next.next
        if not is_cycle:
            return None
        
        head1 = head
        head2 = fast.next
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
