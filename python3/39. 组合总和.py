#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""
典型的回溯算法，这个做法可能不是最优的解法，但是确实work
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(all_paths, path, index, s):
            if s == target:
                all_paths.append(path[:])
                return
            
            if s > target:
                return
            
            for i, cand in enumerate(candidates[index:], index):
                s += cand
                path.append(cand)

                backtrack(all_paths, path, i, s)

                s -= cand
                path.pop()
        
        path = []
        all_paths = []
        candidates = list(sorted(candidates))
        backtrack(all_paths, path, 0, 0)

        return all_paths

