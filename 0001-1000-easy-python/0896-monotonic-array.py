# https://leetcode.com/problems/monotonic-array
class Solution(object):
    # def isMonotonic(self, nums: List[int]) -> bool:
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        direction = nums[-1] - nums[0]
        if (direction == 0):
            for i in range(1, len(nums)):
                if (nums[i] != nums[i-1]):
                    return False
        else:
            for i in range(1, len(nums)):
                if (direction * (nums[i] - nums[i-1]) < 0):
                    return False
        return True

