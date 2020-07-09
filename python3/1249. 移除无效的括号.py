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
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left_indexes = set()
        for index in range(len(s)):
            c = s[index]
            if c == ')':
                if stack and s[stack[-1]] == '(':
                    left_indexes.add(stack.pop())
                    left_indexes.add(index)
            elif c == '(':
                stack.append(index)
            else:
                left_indexes.add(index)
        ans = []
        for i in range(len(s)):
            c = s[i]
            if i in left_indexes:
                ans.append(c)

        return ''.join(ans)

