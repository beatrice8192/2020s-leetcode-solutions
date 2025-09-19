# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (len(nums) == 0):
            return None
        else:
            mid = int(len(nums) / 2)
            return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))

