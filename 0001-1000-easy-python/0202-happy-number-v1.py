# https://leetcode.com/problems/happy-number
class Solution(object):
    # def isHappy(self, n: int) -> bool:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map = {}
        while (n != 1):
            sum = self.getSquareSum(n)
            if (n in map):
                return False
            else:
                map[n] = sum
            n = sum
        return True

    # def getSquareSum(self, n: int) -> int:
    def getSquareSum(self, n):
        sum = 0
        while (n > 0):
            sum += (n % 10) ** 2
            n = int(n / 10)
        return sum
