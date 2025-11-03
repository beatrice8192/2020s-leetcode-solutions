# https://leetcode.com/problems/maximum-average-subarray-i
class Solution(object):
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)
        return float(max_sum) / float(k)

