# https://leetcode.com/problems/reverse-string-ii
class Solution(object):
    # def reverseStr(self, s: str, k: int) -> str:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        for i in range(0, len(s), k * 2):
            result += s[i:(i+k)][::-1] + s[(i+k):(i+k*2)]
        return result

