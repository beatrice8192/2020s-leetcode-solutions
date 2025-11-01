# https://leetcode.com/problems/binary-tree-tilt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def findTilt(self, root: Optional[TreeNode]) -> int:
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root):
            if (root == None):
                return (0, 0) # sum, sum of tilt
            else:
                left = helper(root.left)
                right = helper(root.right)
                return (root.val + left[0] + right[0], abs(left[0] - right[0]) + left[1] + right[1])
        return helper(root)[1]

