# https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if (root == None):
            return False
        else:
            return self.isSameTree(root, subRoot) or \
                self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)

    # referencing the solution of:
    # https://leetcode.com/problems/same-tree
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q == None):
            return True
        elif (p != None and q != None and p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)):
            return True
        else:
            return False

