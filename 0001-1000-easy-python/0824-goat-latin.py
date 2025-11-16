# https://leetcode.com/problems/goat-latin
class Solution(object):
    # def toGoatLatin(self, sentence: str) -> str:
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        words = sentence.split(" ")
        for i in range(len(words)):
            if (words[i][0] not in vowels):
                words[i] = words[i][1:] + words[i][0]
            words[i] += "ma" + "a" * (i + 1)
        return " ".join(words)

