# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        nodes = self.inorderTraversal(root)
        min_diff = sys.maxsize
        for i in range(1, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i-1])
            if (min_diff == 0):
                return 0
        return min_diff

    # referencing the solution of:
    # https://leetcode.com/problems/binary-tree-inorder-traversal
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [] if (root == None) else (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))

