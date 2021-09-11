#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created by m on 2021-09-11
#

"""

"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        ans = []
        while i <= j:
            n1 = nums[i]
            n2 = nums[j]
            if abs(n1) > abs(n2):
                ans.append(n1 ** 2)
                i += 1
            else:
                ans.append(n2 ** 2)
                j -= 1
        ans = ans[::-1]
        return ans


if __name__ == '__main__':
    so = Solution()
