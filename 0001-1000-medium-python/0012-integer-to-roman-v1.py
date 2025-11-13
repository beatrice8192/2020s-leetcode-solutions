# https://leetcode.com/problems/integer-to-roman
class Solution(object):
    # def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            5000: '',
            10000: ''
        }
        result = ""
        digit = 0
        exponent = 0
        while (num > 0):
            digit = num % 10
            num = int(num / 10)
            one = units[1 * (10 ** exponent)]
            five = units[5 * (10 ** exponent)]
            ten = units[10 * (10 ** exponent)]
            result = (one if (digit % 5 == 4) else "") + \
                (ten if digit >= 9 else five if digit >= 4 else "") + \
                (one * (digit % 5) if (digit % 5 != 4) else "") + \
                result
            exponent += 1
        return result

