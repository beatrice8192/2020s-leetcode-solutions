# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.maxDepth(root)[1]

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return (0, 0) # (depth, diameter)
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return (max(left[0], right[0]) + 1, max(left[1], right[1], left[0] + right[0]))

