# https://leetcode.com/problems/balanced-binary-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.maxDepth(root) != -1

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, root):
        if (root == None):
            return 0
        else:
            left = self.maxDepth(root.left)
            if (left == -1):
                return -1
            right = self.maxDepth(root.right)
            if (right == -1 or abs(left - right) > 1):
                return -1
            else:
                return 1 + max(left, right)

