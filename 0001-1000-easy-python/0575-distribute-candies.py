# https://leetcode.com/problems/distribute-candies
class Solution(object):
    # def distributeCandies(self, candyType: List[int]) -> int:
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(set(candyType)), len(candyType) / 2)

