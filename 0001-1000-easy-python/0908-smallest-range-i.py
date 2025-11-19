# https://leetcode.com/problems/smallest-range-i
class Solution(object):
    # def smallestRangeI(self, nums: List[int], k: int) -> int:
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, max(nums) - min(nums) - k * 2)

