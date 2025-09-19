# https://leetcode.com/problems/symmetric-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if (root == None or (root.left == None and root.right == None)):
            return True
        elif (root.left != None and root.right != None and root.left.val == root.right.val and \
            self.isSymmetric(TreeNode(0, root.left.left, root.right.right)) and \
            self.isSymmetric(TreeNode(0, root.left.right, root.right.left))):
            return True
        else:
            return False

