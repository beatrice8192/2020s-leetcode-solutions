# https://leetcode.com/problems/reverse-words-in-a-string-iii
class Solution(object):
    # def reverseWords(self, s: str) -> str:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s[::-1].split(" ")))

