# https://leetcode.com/problems/find-mode-in-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def findMode(self, root: Optional[TreeNode]) -> List[int]:
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        count = {}
        self.inOrderTraversal(root, count)
        max_count = max(count.values())
        return [key for key in count if count[key] == max_count]

    def inOrderTraversal(self, root, count):
        if (root != None):
            self.inOrderTraversal(root.left, count)
            if (root.val not in count):
                count[root.val] = 0
            count[root.val] += 1
            self.inOrderTraversal(root.right, count)

