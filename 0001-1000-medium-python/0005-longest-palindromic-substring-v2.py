# https://leetcode.com/problems/longest-palindromic-substring
class Solution(object):
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        max_start = 0
        for i in range(len(s)):
            left = i
            right = i
            while (right < len(s) - 1 and s[left] == s[right + 1]):
                right += 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    max_start = left
                left -= 1
                right += 1
        return s[max_start:(max_start + max_len)]

