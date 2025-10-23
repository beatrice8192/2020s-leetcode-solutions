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
        nodes = self.preorderTraversal(root)
        subNodes = self.preorderTraversal(subRoot)
        for i in range(0, len(nodes) - len(subNodes) + 1):
            if (nodes[i:(i+len(subNodes))] == subNodes):
                return True
        return False

    # referencing the solution of:
    # https://leetcode.com/problems/binary-tree-preorder-traversal
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def preorderTraversal(self, root):
        """ 
        :type root: TreeNode
        :rtype: List[int]
        """
        return [None] if (root == None) else ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))

