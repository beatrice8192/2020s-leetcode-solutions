# https://leetcode.com/problems/add-digits
class Solution(object):
    # def addDigits(self, num: int) -> int:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (num >= 10):
            digit = 0
            while (num > 0):
                digit += num % 10
                num = int(num / 10)
            num = digit
        return num

