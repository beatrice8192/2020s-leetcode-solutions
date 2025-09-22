# https://leetcode.com/problems/missing-number
class Solution(object):
    # def missingNumber(self, nums: List[int]) -> int:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((len(nums) + 1) * (len(nums)) / 2 - sum(nums))

