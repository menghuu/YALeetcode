#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
pre_head 很重要，很多和链表有关的题目都可以使用这个pre_head节点来解决一些特殊的情况讨论
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre_head = None
        while head:
            next = head.next
            head.next = pre_head
            pre_head = head
            head = next
        return pre_head

