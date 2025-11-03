# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        heap = []
        def dfs(node):
            if (node == None):
                return
            else:
                heapq.heappush(heap, node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        first = heapq.heappop(heap)
        result = first
        while (len(heap) > 0 and result == first):
            result = heapq.heappop(heap)
        return result if result != first else -1

