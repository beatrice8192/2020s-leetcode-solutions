# https://leetcode.com/problems/power-of-four
class Solution(object):
    # def isPowerOfFour(self, n: int) -> bool:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if (n == 1) else \
            (False if (n <= 0 or n & 3 != 0) else \
            self.isPowerOfFour(n >> 2))

