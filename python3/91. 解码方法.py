#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
你再给我一次写的机会我也不能一次性写好

这里需要注意的是: 这里的字符串是有可能不能编码的，所以还需要额外看看哪些返回0的判断条件
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dps = []
        for i in range(len(s)):
            if i == 0:
                if int(s[i]) == 0:
                    return 0
                dps.append(1)
            else:
                n = int(s[i])
                pre_n = int(s[i-1])

                if n == 0:
                    if pre_n == 0 or 10 * pre_n + n > 26:
                        return 0
                    dps.append(dps[-1])
                elif pre_n == 0:
                    dps.append(dps[-1])
                elif 10 * pre_n + n > 26:
                    dps.append(dps[-1])
                elif i + 1 < len(s) and int(s[i+1]) == 0:
                    dps.append(dps[-1])
                elif len(dps) == 1:
                    dps.append(dps[-1] + 1)
                else:
                    dps.append(dps[-1] + dps[-2])
        return dps[-1]
