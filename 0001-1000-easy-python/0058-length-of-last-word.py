# https://leetcode.com/problems/length-of-last-word
class Solution(object):
    # def lengthOfLastWord(self, s: str) -> int:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in reversed(range(len(s))):
            if (s[i] != ' '):
                length += 1
            elif (length > 0):
                break
        return length

