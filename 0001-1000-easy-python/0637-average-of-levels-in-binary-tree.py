# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        levels = []
        def dfs(root, level):
            if (root == None):
                return
            if (len(levels) < level + 1):
                levels.append((0, 0)) # sum, count
            levels[level] = (levels[level][0] + root.val, levels[level][1] + 1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return [float(x[0]) / float(x[1]) for x in levels]

