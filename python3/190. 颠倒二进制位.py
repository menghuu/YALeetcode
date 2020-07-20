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
    def reverseBits(self, n: int) -> int:
        
        ret, power = 0, 31
        while n:
            tmp = (n & 1) << power
            ret += tmp
            n >>= 1
            power -= 1

        return ret
