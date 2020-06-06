#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
比较麻烦的是reversek函数中如果链表长度本身就比k要小的话，实际上，应该不做反转，也就意味着需要再次反转回去
那么这个时候的i的定义就必须严格，之前使用类似
```python
pre_head = None
for i in range(1, k+ 1):
    if not head:
        break
    next = head.next
    head.next = pre_head
    pre_head = head
    head = next
if i != k:
    return self.reversek(pre_head, i)
return pre_head, head
```
就不合适了，这个时候你不知道到底是因为break操作使得跳出了循环还是因为循环条件不满足了跳出循环
并且，因为这个时候i的值永远都是小于等于k的，所以这个时候不能区分
- 因为range条件跳出
- 因为break跳出
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ret_head = ListNode(0)
        ret_head.next = head
        tail = ret_head
        while head:
            reversed_head, next_head = self.reversek(head, k)
            tail.next = reversed_head
            tail = head
            head = next_head
        return ret_head.next

    def reversek(self, head, k):
        pre_head = None
        i = 0
        while i < k and head:
            next = head.next
            head.next = pre_head
            pre_head = head
            head = next
            i += 1
        if i != k:
            return self.reversek(pre_head, i)
        return pre_head, head
