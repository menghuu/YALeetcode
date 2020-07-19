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
    def splitArray(self, nums: List[int], m: int) -> int:
        INIT = float('inf')
        dps = [[INIT for _ in range(len(nums))] for _ in range(m)]
        # dps[i][j] 表示 第i次切割，并且切割在了j位置之后的那个位置，那么这个的最好的结果是什么
        # 这里认为一共会切m 刀，其中最后一刀必须切在末尾

        for i in range(len(dps)):
            # 一共m刀需要切， 现在需要切编号为i的这一刀，需要确定这一刀是切在哪个部位
            # 前面一共切了i刀，那么还剩下m - i刀需要切，切m - i 刀需要后面的m - i 个位置
            right_boundary = len(nums) - 1 - (m - i) + 1
            # 切的第i刀的位置能够取得的最小的选择就是 i， 那么最左侧的边界就应该是 i
            left_boundary = i
            for j in range(i, right_boundary + 1):
                if i == 0 and j == 0:
                    dps[i][j] = nums[j]
                elif i == 0:
                    dps[i][j] = dps[i][j - 1] + nums[j]
                else:
                    # 其实还有一个j == 0的情况，但是由于在这类j的起始值就保证了除非i==0，否则j不可能为0
                    s = sum(nums[left_boundary: j + 1])
                    sum_max = s
                    for left in range(left_boundary, j + 1):
                        sum_max = max(s, dps[i - 1][left - 1])
                        dps[i][j] = min(dps[i][j], sum_max)
                        s -= nums[left]
                    assert s == 0
        return dps[-1][-1]
