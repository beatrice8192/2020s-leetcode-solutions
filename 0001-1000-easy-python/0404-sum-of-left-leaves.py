# https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if (root == None):
            return 0
        else:
            return self.getLeafValue(root.left) + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def getLeafValue(self, node):
        if (node == None or node.left != None or node.right != None):
            return 0
        else:
            return node.val

