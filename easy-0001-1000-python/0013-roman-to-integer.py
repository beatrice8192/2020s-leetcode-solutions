# https://leetcode.com/problems/roman-to-integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        unit = 0
        unit_max = 0
        for i in reversed(range(len(s))):
            unit = self.charToUnit(s[i])
            if unit < 0: return -1
            if unit < unit_max:
                result -= unit
            else:
                unit_max = unit
                result += unit
        return result

    def charToUnit(self, char):
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'L':
            return 50
        elif char == 'C':
            return 100
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000
        else:
            return -1

