#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
别忘记之前的`if len(sc) != len(tc)`的判断
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        if len(sc) != len(tc):
            return False
        for c in sc:
            if sc[c] != tc.get(c, None):
                return False
        return True
