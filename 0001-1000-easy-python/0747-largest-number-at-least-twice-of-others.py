# https://leetcode.com/problems/largest-number-at-least-twice-of-others
class Solution(object):
    # def dominantIndex(self, nums: List[int]) -> int:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted((nums[i], i) for i in range(len(nums)))
        return nums_sorted[-1][1] if nums_sorted[-1][0] >= nums_sorted[-2][0] * 2 else -1

