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
    def isHappy(self, n: int) -> bool:
        def getnext(n):
            ans = 0
            while n:
                n, e = n // 10, n % 10
                ans += e ** 2
            return ans
        
        slow = n
        fast = getnext(n)

        while True:
            slow = getnext(slow)
            fast = getnext(getnext(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
