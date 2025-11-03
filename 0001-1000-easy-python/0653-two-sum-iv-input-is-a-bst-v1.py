# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        return self.twoSum(self.inorderTraversal(root), k)

    # referencing the solution of:
    # https://leetcode.com/problems/two-sum
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while (start < end):
            if (nums[start] + nums[end] < target):
                start += 1
            elif (nums[start] + nums[end] > target):
                end -= 1
            else:
                return True
        return False

    # referencing the solution of:
    # https://leetcode.com/problems/binary-tree-inorder-traversal
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [] if (root == None) else (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))

