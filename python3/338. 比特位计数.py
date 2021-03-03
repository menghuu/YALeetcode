#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
from typing import List, Set, Dict, Tuple

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i // 2] + i % 2)
        return ans
