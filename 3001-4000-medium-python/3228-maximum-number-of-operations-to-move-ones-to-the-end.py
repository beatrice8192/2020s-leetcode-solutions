# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end
class Solution(object):
    # def maxOperations(self, s: str) -> int:
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        ones = 1 if (s[0] == "1") else 0
        for i in range(1, len(s)):
            if (s[i] == "1"):
                ones += 1
            elif (s[i] == "0" and s[i-1] == "1"):
                result += ones
        return result

