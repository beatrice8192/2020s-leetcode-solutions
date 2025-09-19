# https://leetcode.com/problems/climbing-stairs
class Solution(object):
    # using fibonacci
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
