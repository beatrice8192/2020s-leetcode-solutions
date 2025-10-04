# https://leetcode.com/problems/add-strings
class Solution(object):
    # referencing the solution of:
    # https://leetcode.com/problems/add-two-numbers
    # def addStrings(self, num1: str, num2: str) -> str:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        carry = 0
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        while (i1 >= 0):
            carry += int(num1[i1])
            carry += int(num2[i2]) if (i2 >= 0) else 0
            result = str(carry % 10) + result
            carry = int(carry / 10)
            i1 -= 1
            i2 -= 1
        while (i2 >= 0):
            carry += int(num2[i2])
            result = str(carry % 10) + result
            carry = int(carry / 10)
            i2 -= 1
        if (carry != 0):
            result = str(carry % 10) + result
        return result

