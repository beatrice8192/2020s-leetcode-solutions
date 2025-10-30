# https://leetcode.com/problems/power-of-three
class Solution(object):
    # def isPowerOfThree(self, n: int) -> bool:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n == 1) or (n > 1 and n % 3 == 0 and self.isPowerOfThree(int(n / 3)))

