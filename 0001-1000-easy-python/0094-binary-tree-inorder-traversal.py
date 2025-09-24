# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [] if (root == None) else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

