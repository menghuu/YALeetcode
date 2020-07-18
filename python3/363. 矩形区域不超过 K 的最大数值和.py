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
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import math
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        ans = float('-inf')
        for left in range(num_cols):
            row_dps = [0 for _ in range(num_rows)]
            for right in range(left, num_cols):
                for row in range(num_rows):
                    row_dps[row] += matrix[row][right]

                m = float('-inf')
                dps = []
                for top in range(num_rows):
                    if top == 0 or dps[-1] < 0:
                        dps.append(row_dps[top])
                    else:
                        dps.append(dps[-1] + row_dps[top])
                    m = max(m, dps[-1])
                if m <= k:
                    ans = max(ans, m)
                else:
                    for top in range(num_rows):
                        s = 0
                        for bottom in range(top, num_rows):
                            s += row_dps[bottom]
                            if s <= k:
                                ans = max(ans, s)
        return ans
