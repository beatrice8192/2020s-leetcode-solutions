# https://leetcode.com/problems/calculate-money-in-leetcode-bank
class Solution(object):
    # def totalMoney(self, n: int) -> int:
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        quotient = int(n / 7)
        remainder = n % 7
        # ((first complete week) + (last complete week)) * (number of weeks) / 2 +
        # ((first day of last week) + (last day of last week)) * (number of days) / 2
        return ((28) + (28 + (quotient - 1) * 7)) * quotient / 2 + \
            ((quotient + 1) + (quotient + remainder)) * remainder / 2

