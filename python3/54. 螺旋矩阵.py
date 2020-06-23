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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        if not matrix[0]:
            return []

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        ans = []
        while left <= right or top <= bottom:

            if top <= bottom:
                for j in range(left, right + 1):
                    ans.append(matrix[top][j])
                top += 1

            if left <= right:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1

            if top <= bottom:
                for j in range(right, left-1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
