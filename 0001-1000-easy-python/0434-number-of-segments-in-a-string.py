# https://leetcode.com/problems/number-of-segments-in-a-string
class Solution(object):
    # def countSegments(self, s: str) -> int:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while (True):
            while (i < len(s) and s[i] == " "):
                i += 1
            if (i < len(s)):
                count += 1
            else:
                break
            while (i < len(s) and s[i] != " "):
                i += 1
        return count

