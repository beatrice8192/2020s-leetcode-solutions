# https://leetcode.com/problems/move-zeroes

# two pointers
class Solution(object):
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            while (slow < fast and nums[slow] != 0):
                slow += 1
            if (nums[fast] != 0):
                nums[slow], nums[fast] = nums[fast], nums[slow]

