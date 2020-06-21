#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cached = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.pre = self.head

    def _add(self, node):
        head_next = self.head.next
        self.head.next = node
        node.pre = self.head
        head_next.pre = node
        node.next = head_next

    def _delete(self, node):
        if node == self.head or node == self.tail:
            return
        node_pre = node.pre
        node_next = node.next
        node_pre.next = node_next
        node_next.pre = node_pre

    def get(self, key: int) -> int:
        if key in self._cached:
            node = self._cached[key]
            self._delete(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cached:
            node = self._cached[key]
            node.val = value
            node.key = key
            self._delete(node)
            self._add(node)
        else:
            if len(self._cached) == self.capacity:
                last = self.tail.pre
                self._delete(last)
                del self._cached[last.key]
            node = Node()
            node.val = value
            node.key = key
            self._add(node)
            self._cached[key] = node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
