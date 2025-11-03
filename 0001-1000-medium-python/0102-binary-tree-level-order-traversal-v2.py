# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if (root == None):
            return []
        result = []
        def dfs(root, level):
            if (len(result) < level + 1):
                result.append([])
            result[level].append(root.val)
            if (root.left):
                dfs(root.left, level + 1)
            if (root.right):
                dfs(root.right, level + 1)
        dfs(root, 0)
        return result

