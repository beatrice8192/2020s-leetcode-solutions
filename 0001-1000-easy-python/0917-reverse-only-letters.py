# https://leetcode.com/problems/reverse-only-letters
class Solution(object):
    # def reverseOnlyLetters(self, s: str) -> str:
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        s = list(s)
        while (start < end):
            while (start < end and not s[start].isalpha()):
                start += 1
            while (start < end and not s[end].isalpha()):
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)

