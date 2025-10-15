# https://leetcode.com/problems/hamming-distance
class Solution(object):
    # def hammingDistance(self, x: int, y: int) -> int:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        z = x ^ y
        while (z > 0):
            result += z & 1
            z >>= 1
        return result

