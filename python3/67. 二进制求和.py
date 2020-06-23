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
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        for k in range(max(len(a), len(b))):
            i = len(a) - k - 1
            j = len(b) - k - 1

            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0

            sum = (n1 + n2 + carry)
            carry = sum // 2
            sum = sum % 2
            res.insert(0, str(sum))
        if carry == 1:
            res.insert(0, '1')
        return ''.join(res)
