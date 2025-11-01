# https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    # def preorder(self, root: 'Node') -> List[int]:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if (root == None):
            return []
        else:
            return [root.val] + [val for node in root.children for val in self.preorder(node)]

