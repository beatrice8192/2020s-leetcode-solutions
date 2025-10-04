# https://leetcode.com/problems/third-maximum-number
class Solution(object):
    # def thirdMax(self, nums: List[int]) -> int:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        if (len(nums) >= 3):
            return nums[-3]
        else:
            return nums[-1]

