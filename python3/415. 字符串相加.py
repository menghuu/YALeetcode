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
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)

        carry = 0
        ans = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        for index in range(max(l1, l2)):
            if index >= l1:
                s = int(num2[index]) + carry
            elif index >= l2:
                s = int(num1[index]) + carry
            else:
                s = int(num1[index]) + int(num2[index]) + carry
            carry = s // 10
            s %= 10
            ans.append(str(s))
        ans = ''.join(ans[::-1])
        if carry:
            ans = '1' + ans
        return ans

