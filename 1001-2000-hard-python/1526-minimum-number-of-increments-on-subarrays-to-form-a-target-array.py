# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array
class Solution(object):
    # def minNumberOperations(self, target: List[int]) -> int:
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        result = last = 0
        for n in target:
            if (n > last):
                result += n - last
            last = n
        return result

