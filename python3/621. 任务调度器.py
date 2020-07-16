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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counts = list(sorted(Counter(tasks).values()))

        max_val = counts[-1] - 1
        idle = n * max_val

        for val in counts[::-1][1:]:
            idle -= min(max_val, val)
        
        if idle > 0:
            return len(tasks) + idle
        else:
            return len(tasks)


        # n + 1 个为一组，每一组内按照剩余的任务的数量从大到小进行执行任务
        # 为什么是 n + 1 个为一组? 第一个任务执行之后需要 n 个时间恢复，也就是 A 1 2 3 ... n A ...  所以是n+1个为一组
        from collections import Counter
        # 从小到大排列的
        counts = list(sorted(Counter(tasks).values()))
        counts = [0] * (26 - len(counts)) + counts

        ans = 0
        while counts[-1] > 0:
            for i in range(n + 1):
                if counts[-1] == 0:
                    break
                else:
                    if i <= 25 and counts[25 - i] > 0:
                        counts[25 - i] -= 1
                ans += 1
            counts = list(sorted(counts))

        return ans
