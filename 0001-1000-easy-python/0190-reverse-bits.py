# https://leetcode.com/problems/reverse-bits
class Solution(object):
    # def reverseBits(self, n: int) -> int:
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        queue = [0] * 32
        i = 0
        while (n > 0):
            queue[i] = n & 1
            n = n >> 1
            i += 1
        for bit in queue[:-1]:
            result = (result + bit) << 1
        return result + queue[-1]

