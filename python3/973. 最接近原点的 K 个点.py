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
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from collections import deque

        def fn(points, k):
            if k >= len(points):
                dis_with_points = deque(sorted(
                    [(point, point[0] ** 2 + point[1] ** 2) for point in points],
                    key=lambda one: one[1]
                ))

                return dis_with_points

            index = max(1, len(points) // 2)
            dis_with_points1 = fn(points[:index], k)
            dis_with_points2 = fn(points[index:], k)

            dis_with_points = deque()
            while len(dis_with_points) < k:
                if not dis_with_points1:
                    dis_with_points.append(dis_with_points2.popleft())
                elif not dis_with_points2:
                    dis_with_points.append(dis_with_points1.popleft())
                elif dis_with_points1[0][1] < dis_with_points2[0][1]:
                    dis_with_points.append(dis_with_points1.popleft())
                else:
                    dis_with_points.append(dis_with_points2.popleft())
            return dis_with_points

        ans = []

        dis_with_points = fn(points, K)

        while dis_with_points:
            ans.append(dis_with_points.popleft()[0])
        return ans

