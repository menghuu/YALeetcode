#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
没啥好说的，很简单，别忘了最后一个carry
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
        if carry:
            digits.insert(0, 1)
        return digits
