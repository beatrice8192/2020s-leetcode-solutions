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
                if (bfs_queue[i].left):
                    bfs_queue.append(bfs_queue[i].left)
                if (bfs_queue[i].right):
                    bfs_queue.append(bfs_queue[i].right)
            bfs_start = bfs_end
            bfs_end = len(bfs_queue)
        return result

