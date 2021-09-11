#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Created by m on 2021-09-11
#

"""

"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 分成两个部分，后一部分整体往前移动，前一部分整体拷贝到后面
        # 前面一部分的index是[0, l - 1 - k] 或者说 [0, l - k)，或者说，长度是l-k, 那后一部分就是 [1-k, l)了，或者说长度是K

        # 空间复杂度O(1)，时间复杂度O(n)
        l = len(nums)
        k %= l

        start_index = 0
        pre_index = start_index
        pre_value = nums[pre_index]
        swap_counts = 0
        while True:
            index = (pre_index + k) % l
            pre_value, nums[index] = nums[index], pre_value
            swap_counts += 1
            if swap_counts == l:
                break
            else:
                if index == start_index:
                    start_index += 1
                    pre_index = start_index
                    pre_value = nums[pre_index]
                else:
                    pre_index = index

        return

        # 空间复杂度O(1), 时间复杂度O(n)
        # -->+++> [0, l - k) [l-k, l)
        # <+++<-- 翻转一次 [0, k) [k, l)          <===========这里的下标很重要
        # +++><-- 前面反转
        # +++>--> 后面反转

        def reverse(nums, start=0, end=None):
            # [start, end)
            if end is None:
                end = len(nums)
            lo, hi = start, end - 1
            while lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        l = len(nums)
        k %= l

        reverse(nums)
        reverse(nums, 0, k)
        reverse(nums, k, l)

        return

        # 空间复杂度O(n)，时间复杂度O(n)
        l = len(nums)
        k %= l
        tmp = nums[:l-k][:]
        for i in range(l - k, l):
            nums[i - (l - k)] = nums[i]
        for i in range(k, l):
            nums[i] = tmp[i - k]
        return

        # 空间复杂度O(n)，时间复杂度O(n)
        l = len(nums)
        k %= l
        ans = [None] * l
        for i, num in enumerate(nums):
            ans[(i + k) % l] = num
        nums[:] = ans[:]


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    nums = [1, 2, 3, 4, 5]
    k = 2
    # nums = [-1, -100, 3, 99]
    # k = 2
    so.rotate(nums, k)
    print(nums)
    pass
