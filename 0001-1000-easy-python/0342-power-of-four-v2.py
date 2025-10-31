# https://leetcode.com/problems/power-of-four
class Solution(object):
    # def isPowerOfFour(self, n: int) -> bool:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and (n & (n - 1) == 0) and (n.bit_length() & 1 == 1)

