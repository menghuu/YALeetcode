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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        lower_sums = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                lower_sums[j] = min(lower_sums[j], lower_sums[j + 1]) + triangle[i][j]
            lower_sums.pop()
        
        return lower_sums[0]
