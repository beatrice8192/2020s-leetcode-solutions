# https://leetcode.com/problems/counting-bits
class Solution(object):
    # def countBits(self, n: int) -> List[int]:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for i in range(n + 1):
            mask = 1
            while (mask <= i):
                if (i & mask == mask):
                    result[i] += 1
                mask <<= 1
        return result

