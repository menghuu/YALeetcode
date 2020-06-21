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
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            lc = s[left].lower()
            rc = s[right].lower()

            if not lc.isalnum():
                left += 1
            elif not rc.isalnum():
                right -= 1
            elif lc == rc:
                left += 1
                right -= 1
            else:
                return False
        return True
