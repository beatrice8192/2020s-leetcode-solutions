# https://leetcode.com/problems/largest-triangle-area
# https://en.wikipedia.org/wiki/Area_of_a_triangle
class Solution(object):
    # def largestTriangleArea(self, points: List[List[int]]) -> float:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        for p1 in range(len(points)):
            x1, y1 = points[p1]
            for p2 in range(p1 + 1, len(points)):
                x2, y2 = points[p2]
                for p3 in range(p2 + 1, len(points)):
                    x3, y3 = points[p3]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    max_area = max(max_area, area)
        return 0.5 * max_area

