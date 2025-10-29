# https://leetcode.com/problems/smallest-number-with-all-set-bits
class Solution(object):
    # def smallestNumber(self, n: int) -> int:
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1 << n.bit_length()) - 1

