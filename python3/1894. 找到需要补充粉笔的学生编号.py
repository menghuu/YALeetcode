#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <mail@meng.hu>

"""

"""

from bisect import bisect_right
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, n in enumerate(chalk):
            if k < n:
                return i
            k -= n
            assert k >= 0

        n = len(chalk)
        if chalk[0] > k:
            return 0
        for i in range(1, n):
            chalk[i] += chalk[i-1]
            if chalk[i] > k:
                return i

        k %= chalk[-1]
        return bisect_right(chalk, k)

        i = 0
        while True:
            k -= chalk[i]
            if k < 0:
                return i
            i += 1
            i %= len(chalk)


if __name__ == '__main__':
    so = Solution()

    chalk = [5, 1, 5]
    k = 22
    ans = so.chalkReplacer(chalk=chalk, k=k)
    print(ans)
