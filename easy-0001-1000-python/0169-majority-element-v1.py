# https://leetcode.com/problems/majority-element
class Solution(object):
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for n in nums:
            if (n not in hash):
                hash[n] = 0
            hash[n] += 1
            if (hash[n] > len(nums) / 2):
                return n

