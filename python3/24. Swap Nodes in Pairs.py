#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
其实链表的题目中，构建一个假的头结点十分常见
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret_head = ListNode(0)
        
        pre_head = ret_head
        
        while head and head.next:
            next = head.next
            nextnext = next.next
            pre_head.next = next
            next.next = head
            head.next = None

            pre_head = head
            head = nextnext
        if head:
            pre_head.next = head
        return ret_head.next

