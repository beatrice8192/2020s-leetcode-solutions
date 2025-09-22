# https://leetcode.com/problems/power-of-three
class Solution(object):
    # def isPowerOfThree(self, n: int) -> bool:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if (n == 1) else \
            (False if (n <= 0 or n % 3 != 0) else \
            self.isPowerOfThree(int(n / 3)))

