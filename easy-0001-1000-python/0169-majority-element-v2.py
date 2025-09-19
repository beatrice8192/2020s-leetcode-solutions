# https://leetcode.com/problems/majority-element
class Solution(object):
    # Moore's Voting Algorithm
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = 0
        for n in nums:
            if (count == 0):
                candidate = n
            if (n == candidate):
                count += 1
            else:
                count -= 1
        return candidate

