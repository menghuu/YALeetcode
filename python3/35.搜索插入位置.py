#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created by m on 2021-09-10
#

"""

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            num = nums[mi]
            if num == target:
                return mi
            elif target < num:
                hi = mi - 1
            else:
                lo = mi + 1
        return (lo + hi + 1) // 2


if __name__ == '__main__':
    pass
