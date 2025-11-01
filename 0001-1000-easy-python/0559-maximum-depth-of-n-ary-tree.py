# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    # def maxDepth(self, root: 'Node') -> int:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if (root == None):
            return 0
        elif (len(root.children) == 0):
            return 1
        else:
            return 1 + max([self.maxDepth(child) for child in root.children])

