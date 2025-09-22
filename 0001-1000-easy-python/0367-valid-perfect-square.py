# https://leetcode.com/problems/valid-perfect-square
# referencing the solution of:
# https://leetcode.com/problems/sqrtx
class Solution(object):
    # def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == self.mySqrt(num) ** 2
        
    # def mySqrt(self, x: int) -> int:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = x
        while not (sqrt * sqrt <= x and (sqrt + 1) * (sqrt + 1) >= x):
            sqrt = int((sqrt + x / sqrt) / 2)
        return sqrt

