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
    def countBits(self, num: int) -> List[int]:
        import math
        if num == 0:
            return [0]
        ans = [0, 1]
        for power in range(1, int(math.log(num, 2)) + 1):
            base = 2 ** power
            for i in range(base, base * 2):
                if i > num:
                    break
                else:
                    ans.append(1 + ans[i - base])
        return ans

