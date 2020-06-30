#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class CQueue:

    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        while self.stack:
            self.tmp_stack.append(self.stack.pop())
        if not self.tmp_stack:
            return -1
        num = self.tmp_stack.pop()
        while self.tmp_stack:
            self.stack.append(self.tmp_stack.pop())
        return num

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
