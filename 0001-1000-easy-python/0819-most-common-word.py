# https://leetcode.com/problems/most-common-word
class Solution(object):
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        occurrences = {}
        paragraph = paragraph.lower()
        banned = set(banned)
        i = 0
        while (i < len(paragraph)):
            while (i < len(paragraph) and not paragraph[i].isalnum()): # not alpha-numeric
                i += 1
            j = i
            while (i < len(paragraph) and paragraph[i].isalnum()): # is alpha-numeric
                i += 1
            word = paragraph[j:i]
            if (word not in occurrences):
                occurrences[word] = 0
            occurrences[word] += 1
        frequencies = list(reversed(sorted([(occurrences[word], word) for word in occurrences])))
        for f in frequencies:
            if (f[1] not in banned):
                return f[1]
        return None

