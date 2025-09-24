# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if (root == None):
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

