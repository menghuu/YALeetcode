#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created by m on 2021-09-10
#

"""

"""

from typing import List


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mi = (lo + hi) // 2
            if isBadVersion(mi):
                hi = mi - 1
            else:
                lo = mi + 1

        mi = (lo + hi + 1) // 2
        return mi


if __name__ == '__main__':
    pass
