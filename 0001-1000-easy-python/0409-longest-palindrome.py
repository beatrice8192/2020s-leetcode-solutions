# https://leetcode.com/problems/longest-palindrome
class Solution(object):
    # def longestPalindrome(self, s: str) -> int:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        map = {}
        hasOdd = False
        for char in s:
            if (char not in map):
                map[char] = 0
            map[char] += 1
        for char in map.keys():
            if (map[char] % 2 == 1):
                hasOdd = True
            result += int(map[char] / 2) * 2
        return result + (1 if (hasOdd) else 0)

