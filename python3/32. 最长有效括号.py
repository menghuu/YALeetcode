#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
动态规划和栈应用到一块，重点在那个 `stack and c ==')'`条件下的更新状态上
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        dps = [0 for _ in s]
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if stack and c == '(':
                stack.append(i)
            elif stack and c == ')':
                dps[i] = 1 + dps[i - 1]
                index = stack.pop()
                if index != 0:
                    dps[i] += dps[index - 1]
            elif c == '(':
                stack.append(i)
            ans = max(ans, dps[i])
        return ans * 2
