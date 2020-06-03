#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
没啥好说的，就是别忘记把tail = tail.next 的操作
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val >= l2.val:
            # 保证l1的值比较小
            l1, l2 = l2, l1
        head = l1
        tail = l1
        l1 = l1.next
        while l1 or l2:
            if not l1:
                tail.next = l2
                break
            if not l2:
                tail.next = l1
                break
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return head
