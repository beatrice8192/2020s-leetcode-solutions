# https://leetcode.com/problems/detect-capital
class Solution(object):
    # def detectCapitalUse(self, word: str) -> bool:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word == upper(word)) or (word == lower(word)) or (word[1:] == lower(word[1:]))

