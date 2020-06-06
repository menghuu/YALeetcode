#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution:
    def isValid(self, s: str) -> bool:
        from queue import deque
        stack = deque()
        for c in s:
            if c == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif c in '([{':
                stack.append(c)
            else:
                return False
        return not stack
