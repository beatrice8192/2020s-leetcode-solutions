# https://leetcode.com/problems/ugly-number
class Solution(object):
    # def isUgly(self, n: int) -> bool:
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return False
        while (n & 1 == 0):
            n >>= 1
        while (n % 3 == 0):
            n = int(n / 3)
        while (n % 5 == 0):
            n = int(n / 5)
        return n == 1

