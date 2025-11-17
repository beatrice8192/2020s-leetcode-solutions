# https://leetcode.com/problems/binary-gap
class Solution(object):
    # def binaryGap(self, n: int) -> int:
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_gap = 0
        last_one = -1
        i = 0
        while (n > 0):
            if (n & 1 == 1):
                if (last_one != -1):
                    max_gap = max(max_gap, i - last_one)
                last_one = i
            n >>= 1
            i += 1
        return max_gap

