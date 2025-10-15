# https://leetcode.com/problems/max-consecutive-ones
class Solution(object):
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_one = 0
        curr_one = 0
        for n in nums:
            if (n == 1):
                curr_one += 1
                max_one = max(max_one, curr_one)
            else:
                curr_one = 0
        return max_one

