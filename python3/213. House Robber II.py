#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
就相当于最后一个到底选不选，选的话，那么第一个就不能选，那么就将dps[0][1] 设置成 0
那么如果只有一个元素的时候需要特殊考虑。
还有因为没有特殊的初始化，所以特殊考虑长度等于0的时候的情况
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0
        dps1 = []
        dps2 = []
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                dps1.append([0, 0])
                dps2.append([0, num])
            else:
                dps1.append([
                    max(dps1[-1]),
                    dps1[-1][0] + num
                ])
                dps2.append([
                    max(dps2[-1]),
                    dps2[-1][0] + num
                ])
        m1 = dps1[-1][1]
        m2 = dps2[-1][0]
        return max(m1, m2)
