# https://leetcode.com/problems/shortest-completing-word
class Solution(object):
    # def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        occurrences = {}
        licensePlate = lower(licensePlate)
        words = sorted(words, key=len)
        for char in licensePlate:
            if (char.isalpha()):
                if (char not in occurrences):
                    occurrences[char] = 0
                occurrences[char] += 1
        def invalid(word, char):
            return char not in word or (occurrences[char] > 1 and occurrences[char] != word.count(char))
        for word in words:
            if (len([char for char in occurrences if invalid(word, char)]) == 0):
                return word
        return ""

