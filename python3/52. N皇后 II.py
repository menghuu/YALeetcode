#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
这一题本意是用bitmap来做的，有兴趣的可以参看leetcode的官方解答
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def backtrack(row, columns: set, xy_diff: list, xy_sum: list):
            if row == n:
                self.ans += 1
            else:
                for col in columns:
                    if xy_diff[row - col] and xy_sum[row + col]:
                        xy_diff[row - col] = False
                        xy_sum[row + col] = False

                        backtrack(row + 1, columns.difference({col}), xy_diff, xy_sum)

                        xy_diff[row - col] = True
                        xy_sum[row + col] = True

        columns = set(range(n))
        xy_diff = [True for _ in range(2 * n - 1)]
        xy_sum = [True for _ in range(2 * n - 1)]

        backtrack(0, columns, xy_diff, xy_sum)

        return self.ans

