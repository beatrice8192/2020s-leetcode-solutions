# https://leetcode.com/problems/fibonacci-number
class Solution(object):
    # def fib(self, n: int) -> int:
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if (n == 0 or n == 1) else self.fib(n - 1) + self.fib(n - 2)

