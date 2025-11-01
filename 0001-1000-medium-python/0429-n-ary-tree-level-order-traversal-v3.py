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
        if root == None:
            return []
        result = []
        get_children = lambda node: node.children
        bfs = BFS(root, get_children)
        while bfs.hasNext():
            node = bfs.getNext()
            if (len(result) <= bfs.level):
                result.append([])
            result[bfs.level].append(node.val)
        return result

class BFS:
    def __init__(self, root, get_children):
        self.get_children = get_children
        self.bfs_queue = [root]
        self.bfs_start = 0
        self.bfs_end = len(self.bfs_queue)
        self.index = 0
        self.level = 0

    def hasNext(self):
        if (self.index == self.bfs_end):
            self.bfs_start = self.bfs_end
            self.bfs_end = len(self.bfs_queue)
            self.level += 1
        return self.bfs_start < self.bfs_end

    def getNext(self):
        node = self.bfs_queue[self.index]
        self.bfs_queue.extend(self.get_children(node))
        self.index += 1
        return node

