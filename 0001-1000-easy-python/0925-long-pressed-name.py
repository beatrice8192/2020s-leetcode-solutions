# https://leetcode.com/problems/long-pressed-name
class Solution(object):
    # def isLongPressedName(self, name: str, typed: str) -> bool:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if (name[0] != typed[0]):
            return False
        n = 1
        t = 1
        while (n < len(name) and t < len(typed)):
            while (t < len(typed) and typed[t] != name[n] and typed[t] == typed[t-1]):
                t += 1
            if (t == len(typed) or typed[t] != name[n]):
                return False
            n += 1
            t += 1
        while (t < len(typed) and typed[t] == typed[t-1]):
            t += 1
        return n == len(name) and t == len(typed)

