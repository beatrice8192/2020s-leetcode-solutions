# https://leetcode.com/problems/integer-to-roman
class Solution(object):
    # def intToRoman(self, num: int) -> str:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        result = ""
        for tup in units:
            while (num >= tup[0]):
                num -= tup[0]
                result += tup[1]
        return result

