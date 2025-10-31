# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville
class Solution(object):
    # def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        occurrence = [False] * (len(nums) - 2)
        for n in nums:
            if (not occurrence[n]):
                occurrence[n] = True
            else:
                result.append(n)
        return result

