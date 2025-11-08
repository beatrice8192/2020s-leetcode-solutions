# https://leetcode.com/problems/count-binary-substrings
class Solution(object):
    # def countBinarySubstrings(self, s: str) -> int:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        array = [1]
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                array[-1] += 1
            else:
                array.append(1)
        for i in range(1, len(array)):
            result += min(array[i], array[i-1])
        return result

