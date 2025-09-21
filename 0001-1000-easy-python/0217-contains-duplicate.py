# https://leetcode.com/problems/contains-duplicate
class Solution(object):
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for n in nums:
            if (n in map):
                return True
            else:
                map[n] = True
        return False

