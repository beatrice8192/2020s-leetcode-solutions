# https://leetcode.com/problems/base-7
class Solution(object):
    # def convertToBase7(self, num: int) -> str:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num == 0):
            return "0"
        result = ""
        isNegative = num < 0
        num = abs(num)
        while (num > 0):
            result = str(num % 7) + result
            num = int(num / 7)
        return ("-" if isNegative else "") + result

