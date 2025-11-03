# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        nums = set()
        def dfs(node):
            if (node == None):
                return False
            else:
                if (k - node.val in nums):
                    return True
                nums.add(node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)

