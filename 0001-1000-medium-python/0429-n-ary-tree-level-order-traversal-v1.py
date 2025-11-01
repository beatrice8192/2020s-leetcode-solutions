# https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    # referencing the solution of:
    # https://leetcode.com/problems/binary-tree-level-order-traversal
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if (root == None):
            return []
        result = []
        bfs_queue = [root]
        bfs_start = 0
        bfs_end = len(bfs_queue)
        while (bfs_start < bfs_end):
            result.append([])
            for i in range(bfs_start, bfs_end):
                result[-1].append(bfs_queue[i].val)
                bfs_queue.extend(bfs_queue[i].children)
            bfs_start = bfs_end
            bfs_end = len(bfs_queue)
        return result

