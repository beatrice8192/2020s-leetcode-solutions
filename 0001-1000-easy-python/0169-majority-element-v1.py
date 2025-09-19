# https://leetcode.com/problems/majority-element
class Solution(object):
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for n in nums:
            if (n not in map):
                map[n] = 0
            map[n] += 1
            if (map[n] > len(nums) / 2):
                return n

