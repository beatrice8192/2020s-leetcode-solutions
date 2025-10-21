# https://leetcode.com/problems/relative-ranks
class Solution(object):
    # def findRelativeRanks(self, score: List[int]) -> List[str]:
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        map = {}
        rank = len(score)
        for s in sorted(score):
            map[s] = rank
            rank -= 1
        return [(str(map[x]) if map[x] > 3 else medals[map[x] - 1]) for x in score]

