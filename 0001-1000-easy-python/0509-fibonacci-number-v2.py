# https://leetcode.com/problems/fibonacci-number
class Solution(object):
    # def fib(self, n: int) -> int:
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {0: 0, 1: 1}
        return self.memoizedFib(n, memory)

    def memoizedFib(self, n, memory):
        if (n not in memory):
            memory[n] = self.memoizedFib(n - 1, memory) + self.memoizedFib(n - 2, memory)
        return memory[n]

