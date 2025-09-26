# https://leetcode.com/problems/string-to-integer-atoi
class Solution(object):
    DIGITS = ['0','1','2','3','4','5','6','7','8','9']

    # def myAtoi(self, s: str) -> int:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        def truncateInteger(result, positive):
            if (positive):
                return min(result, 2 ** 31 - 1)
            else:
                return -min(result, 2 ** 31) 
        result = 0 
        positive = True
        terminate = False
        for i in range(len(s)):
            if (s[i] in self.DIGITS):
                digit = ord(s[i]) - 48
                result = result * 10 + digit
                terminate = True
            elif (terminate):
                break
            elif (s[i] == '-'):
                terminate = True
                positive = False
            elif (s[i] == '+'):
                terminate = True
            elif (s[i] == ' '):
                pass
            else:
                break
        return truncateInteger(result, positive)

