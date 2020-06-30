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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists.pop()
        elif len(lists) == 0:
            return None

        l1 = lists.pop(0)
        l2 = lists.pop(0)

        head = ListNode(0)
        current = head

        while l1 or l2:
            if not l1:
                current.next, current = l2, current.next
                break
            elif not l2:
                current.next, current = l1, current.next
                break
            elif l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
                current.next = None
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
                current.next = None

        lists.append(head.next)
        return self.mergeKLists(lists)

