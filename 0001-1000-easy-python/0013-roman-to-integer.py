# https://leetcode.com/problems/roman-to-integer
class Solution(object):
    UNITS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        unit = 0
        unit_max = 0
        for i in reversed(range(len(s))):
            unit = self.UNITS[s[i]]
            if (unit < unit_max):
                result -= unit
            else:
                unit_max = unit
                result += unit
        return result

