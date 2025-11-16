# https://leetcode.com/problems/backspace-string-compare
class Solution(object):
    # def backspaceCompare(self, s: str, t: str) -> bool:
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def backspace(str, i):
            stack = 0
            while (i >= 0 and (str[i] == "#" or stack > 0)):
                if (str[i] == "#"):
                    stack += 1
                elif (stack > 0):
                    stack -= 1
                i -= 1
            return i
        si = len(s) - 1
        ti = len(t) - 1
        while (si >= 0 and ti >= 0):
            si = backspace(s, si)
            ti = backspace(t, ti)
            if (si < 0 or ti < 0):
                break
            elif (si >= 0 and ti >= 0 and s[si] != t[ti]):
                return False
            si -= 1
            ti -= 1
        si = backspace(s, si)
        ti = backspace(t, ti)
        return (si < 0 and ti < 0)

