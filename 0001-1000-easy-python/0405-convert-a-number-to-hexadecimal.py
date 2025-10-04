# https://leetcode.com/problems/convert-a-number-to-hexadecimal
class Solution(object):
    # def toHex(self, num: int) -> str:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        if (num == 0):
            return "0"
        if (num < 0):
            num = 2 ** 32 + num
        while (num > 0):
            digit = num % 16
            if (digit < 10):
                result = str(digit) + result
            else:
                result = chr(digit - 10 + 97) + result
            num >>= 4
        return result

