# https://leetcode.com/problems/array-partition
class Solution(object):
    # def arrayPairSum(self, nums: List[int]) -> int:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([nums[i] for i in range(0, len(nums), 2)])

