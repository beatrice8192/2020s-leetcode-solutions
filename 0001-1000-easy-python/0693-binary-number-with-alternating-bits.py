# https://leetcode.com/problems/binary-number-with-alternating-bits
class Solution(object):
    # def hasAlternatingBits(self, n: int) -> bool:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        xor = n ^ (n >> 1)
        return xor & (xor + 1) == 0

