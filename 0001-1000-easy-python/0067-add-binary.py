# https://leetcode.com/problems/add-binary
class Solution(object):
    # def addBinary(self, a: str, b: str) -> str:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        i = 1
        while (i <= len(a) or i <= len(b)):
            if (i <= len(a) and a[-i] == "1"):
                carry += 1
            if (i <= len(b) and b[-i] == "1"):
                carry += 1
            result = str(carry % 2) + result
            carry = int(carry / 2)
            i += 1
        if (carry == 1):
            result = "1" + result
        return result

