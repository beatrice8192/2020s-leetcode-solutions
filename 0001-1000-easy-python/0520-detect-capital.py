# https://leetcode.com/problems/detect-capital
class Solution(object):
    # def detectCapitalUse(self, word: str) -> bool:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word == word.upper()) or (word == word.lower()) or (word[1:] == word[1:].lower())

