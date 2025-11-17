# https://leetcode.com/problems/uncommon-words-from-two-sentences
class Solution(object):
    # def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        occurrences1 = {}
        occurrences2 = {}
        for word in words1:
            if (word not in occurrences1):
                occurrences1[word] = 0
            occurrences1[word] += 1
        for word in words2:
            if (word not in occurrences2):
                occurrences2[word] = 0
            occurrences2[word] += 1
        return [word for word in occurrences1 if occurrences1[word] == 1 and word not in occurrences2] + \
            [word for word in occurrences2 if occurrences2[word] == 1 and word not in occurrences1]

