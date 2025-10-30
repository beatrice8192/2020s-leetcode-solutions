# https://leetcode.com/problems/power-of-four
class Solution(object):
    # def isPowerOfFour(self, n: int) -> bool:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n == 1) or (n > 1 and n % 4 == 0 and self.isPowerOfFour(int(n / 4)))

