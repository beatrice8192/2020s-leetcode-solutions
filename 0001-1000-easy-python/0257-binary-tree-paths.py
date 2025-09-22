# https://leetcode.com/problems/binary-tree-paths
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if (root == None):
            return []
        elif (root.left == None and root.right == None):
            return [str(root.val)]
        else:
            return [("%d->%s" % (root.val, x)) for x in self.binaryTreePaths(root.left)] + [("%d->%s" % (root.val, x)) for x in self.binaryTreePaths(root.right)]

