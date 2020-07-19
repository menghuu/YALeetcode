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
    def checkRecord(self, n: int) -> int:
        magic_num = 10 ** 9 + 7
        LLA, YLA, YA, LL, PL, P = 0, 0, 1, 0, 1, 1
        # Y 代表任意不为L的字母，可以是A也可以时P
        # X 表示任意的字符
        # 如果最后一个字母是A，则表示这一串字符串中包含一个A
        for i in range(1, n):
            LLA_, YLA_, YA_, LL_, PL_, P_ = YLA, YA, (LLA + YLA + YA + LL + PL + P) % magic_num, PL, P, (LL + PL + P) % magic_num

            LLA, YLA, YA, LL, PL, P = LLA_, YLA_, YA_, LL_, PL_, P_

        return (LLA + YLA + YA + LL + PL + P) % magic_num

