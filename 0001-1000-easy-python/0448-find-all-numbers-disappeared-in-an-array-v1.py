# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
class Solution(object):
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mask = [False] * len(nums)
        for n in nums:
            mask[n - 1] = True
        return [i + 1 for i in range(len(nums)) if not mask[i]]

