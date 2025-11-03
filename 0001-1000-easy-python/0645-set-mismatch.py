# https://leetcode.com/problems/set-mismatch
class Solution(object):
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        occurrences = [0] * len(nums)
        for i in range(len(nums)):
            occurrences[nums[i] - 1] += 1
        return [i + 1 for i in range(len(nums)) if occurrences[i] == 2] + [i + 1 for i in range(len(nums)) if occurrences[i] == 0]

