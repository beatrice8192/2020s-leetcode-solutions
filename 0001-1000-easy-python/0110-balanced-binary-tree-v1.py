# https://leetcode.com/problems/balanced-binary-tree
# referencing the solution of:
# https://leetcode.com/problems/maximum-depth-of-binary-tree

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
        if (root == None):
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and \
                abs(self.maxDepth(root.left) - self.maxDepth(root.right)) < 2

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

