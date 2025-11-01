# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        bfs_queue = [root]
        bfs_start = 0
        bfs_end = len(bfs_queue)
        level = 1
        while (bfs_start < bfs_end):
            for i in range(bfs_start, bfs_end):
                if (bfs_queue[i].left == None and bfs_queue[i].right == None):
                    return level
                if (bfs_queue[i].left != None):
                    bfs_queue.append(bfs_queue[i].left)
                if (bfs_queue[i].right != None):
                    bfs_queue.append(bfs_queue[i].right)
            bfs_start = bfs_end
            bfs_end = len(bfs_queue)
            level += 1
        return level

