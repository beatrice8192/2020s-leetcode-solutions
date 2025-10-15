# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations
class Solution(object):
    # def findSmallestInteger(self, nums: List[int], value: int) -> int:
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        count = [0] * value
        for i in range(len(nums)):
            count[nums[i] % value] += 1
        min_count = sys.maxsize
        min_i = -1
        for i in range(value):
            if (count[i] < min_count):
                min_count = count[i]
                min_i = i
        return value * min_count + min_i

