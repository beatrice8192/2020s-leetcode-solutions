# https://leetcode.com/problems/number-of-1-bits
class Solution(object):
    # def hammingWeight(self, n: int) -> int:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        while (n > 0):
            ones += n & 1
            n >>= 1
        return ones

