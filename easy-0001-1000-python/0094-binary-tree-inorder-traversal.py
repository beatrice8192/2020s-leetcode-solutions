# https://leetcode.com/problems/binary-tree-inorder-traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        if root.left != None:
            result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right != None:
            result.extend(self.inorderTraversal(root.right))
        return result

