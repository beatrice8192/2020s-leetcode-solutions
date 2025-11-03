# https://leetcode.com/problems/longest-continuous-increasing-subsequence
class Solution(object):
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_len = 1
        max_len = 1
        for i in range(len(nums) - 1):
            if (nums[i+1] > nums[i]):
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
        return max_len

