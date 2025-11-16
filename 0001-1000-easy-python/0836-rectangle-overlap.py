# https://leetcode.com/problems/rectangle-overlap
class Solution(object):
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return min(x1, x2) < max(x3, x4) and min(x3, x4) < max(x1, x2) and \
            min(y1, y2) < max(y3, y4) and min(y3, y4) < max(y1, y2)

