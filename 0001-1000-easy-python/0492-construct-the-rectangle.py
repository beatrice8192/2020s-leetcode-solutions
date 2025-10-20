# https://leetcode.com/problems/construct-the-rectangle
class Solution(object):
    # def constructRectangle(self, area: int) -> List[int]:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = int(area ** 0.5)
        while (width > 1):
            if (area % width == 0):
                return [int(area / width), width]
            width -= 1
        return [area, 1]

