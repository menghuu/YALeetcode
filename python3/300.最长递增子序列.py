#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 m <m@meng.hu>
#
# Distributed under terms of the MIT license.

"""

"""
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？ 
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1399 👎 0


from typing import List, Set, Dict, Tuple


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 时间复杂度为O(n*log(n))
        # dp[i] 表示最长递增子序列长度为i+1时，末尾的数字**最小**是多少
        # 这里还隐含dp是一个递增的数组的表达
        dp = [nums[0]]
        for num in nums[1:]:
            if num > dp[-1]:
                # 也就是说num这个数字可以跟在前一个最长子序列的后面
                dp.append(num)
            elif num == dp[-1]:
                continue
            else:
                # 在dp数组中找到第一个大于等于num的数字的index，使用二分查找的方式来做
                # 对于二分查找，可以查看https://www.bilibili.com/video/BV1d54y1q7k7
                lo, hi = -1, len(dp)
                while lo + 1 != hi:
                    mi = (lo + hi) // 2
                    if dp[mi] < num:
                        lo = mi
                    else:
                        hi = mi
                dp[hi] = num
        return len(dp)

        # 时间复杂度为O(n**2)
        # dp[i] 表示以nums[i] 为结尾的话，递增子序列的**最长**长度是多少
        dp = [1]
        ans = 1
        for i in range(1, len(nums)):
            dp.append(1)
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[-1] = max(dp[-1], dp[j] + 1)
            ans = max(ans, dp[-1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    so = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [0, 1, 0, 3, 2, 3]
    nums = [7, 7, 7, 7, 7, 7, 7]
    # nums = [4, 10, 4, 3, 8, 9]
    ans = so.lengthOfLIS(nums)
    print(ans)

