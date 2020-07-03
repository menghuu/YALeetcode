# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def dac(nums, start, end):
            if start > end:
                return None

            middle = (start + end) // 2
            root = TreeNode(nums[middle])
            root.left = dac(nums, start, middle-1)
            root.right = dac(nums, middle+1, end)
            return root
        
        root = dac(nums, 0, len(nums)-1)

        return root
