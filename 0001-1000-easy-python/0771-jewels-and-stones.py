# https://leetcode.com/problems/jewels-and-stones
class Solution(object):
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = set(list(jewels))
        return len([x for x in list(stones) if x in jewels])

