# https://leetcode.com/problems/sort-array-by-parity
class Solution(object):
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while (start < end):
            while (start < end and nums[start] & 1 == 0):
                start += 1
            while (start < end and nums[end] & 1 == 1):
                end -= 1
            nums[start], nums[end] = nums[end], nums[start]
        return nums

