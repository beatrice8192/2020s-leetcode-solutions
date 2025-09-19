# https://leetcode.com/problems/path-sum
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # bfs
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if (root == None):
            return False
        queue = [root]
        start = 0
        end = len(queue)
        while (start < end):
            for i in range(start, end):
                if (queue[i].val == targetSum and queue[i].left == None and queue[i].right == None):
                    return True
                if (queue[i].left != None):
                    queue[i].left.val += queue[i].val
                    queue.append(queue[i].left)
                if (queue[i].right != None):
                    queue[i].right.val += queue[i].val
                    queue.append(queue[i].right)
            start = end
            end = len(queue)
        return False

