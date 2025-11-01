# https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution(object):
    # def postorder(self, root: 'Node') -> List[int]:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if (root == None):
            return []
        else:
            return [val for node in root.children for val in self.postorder(node)] + [root.val]

