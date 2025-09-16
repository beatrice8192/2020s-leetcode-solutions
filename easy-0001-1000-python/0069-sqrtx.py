# https://leetcode.com/problems/sqrtx
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x
        while not (result * result <= x and (result + 1) * (result + 1) >= x):
            result = (result + x / result) / 2
        return result

