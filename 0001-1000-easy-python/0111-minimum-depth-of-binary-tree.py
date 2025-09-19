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
        # bfs
        if (root == None):
            return 0
        queue = [root]
        depth = 1
        start = 0
        end = len(queue)
        while (start < end):
            for i in range(start, end):
                if (queue[i].left == None and queue[i].right == None):
                    return depth
                if (queue[i].left != None):
                    queue.append(queue[i].left)
                if (queue[i].right != None):
                    queue.append(queue[i].right)
            start = end
            end = len(queue)
            depth += 1
        return depth

