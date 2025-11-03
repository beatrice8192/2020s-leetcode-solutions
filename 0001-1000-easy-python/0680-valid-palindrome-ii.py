# https://leetcode.com/problems/valid-palindrome-ii
class Solution(object):
    # def validPalindrome(self, s: str) -> bool:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(str):
            start = 0
            end = len(str) - 1
            while (start < end and str[start] == str[end]):
                start += 1
                end -= 1
            return str[start] == str[end]
        start = 0
        end = len(s) - 1
        while (start < end and s[start] == s[end]):
            start += 1
            end -= 1
        return s[start] == s[end] or isPalindrome(s[start:end]) or isPalindrome(s[start+1:end+1])

