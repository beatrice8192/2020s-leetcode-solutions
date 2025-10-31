# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array
class Solution(object):
    # def minNumberOperations(self, target: List[int]) -> int:
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        result = prev = 0
        for n in target:
            if (n > prev):
                result += n - prev
            prev = n
        return result

