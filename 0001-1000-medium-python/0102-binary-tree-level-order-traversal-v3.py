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
        if root == None:
            return []
        result = []
        get_children = lambda node: ([node.left] if node.left else []) + ([node.right] if node.right else [])
        bfs = TreeBFS(root, get_children)
        while bfs.hasNext():
            top = bfs.getNext()
            if (len(result) <= bfs.level):
                result.append([])
            result[bfs.level].append(top.val)
        return result

class TreeBFS:
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
            self.index = self.bfs_start
            self.level += 1
        return self.bfs_start < self.bfs_end

    def getNext(self):
        top = self.bfs_queue[self.index]
        self.bfs_queue.extend(self.get_children(top))
        self.index += 1
        return top

