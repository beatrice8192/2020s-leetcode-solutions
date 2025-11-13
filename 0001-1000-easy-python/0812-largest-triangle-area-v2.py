# https://leetcode.com/problems/largest-triangle-area
# https://en.wikipedia.org/wiki/Area_of_a_triangle
class Solution(object):
    # def largestTriangleArea(self, points: List[List[int]]) -> float:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_cross_product = 0
        for p1 in range(len(points)):
            x1, y1 = points[p1]
            for p2 in range(p1 + 1, len(points)):
                x2, y2 = points[p2]
                for p3 in range(p2 + 1, len(points)):
                    x3, y3 = points[p3]
                    # cross product magnitude of vectors (p1->p2) and (p1->p3)
                    cross_product = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
                    max_cross_product = max(max_cross_product, cross_product)
        return 0.5 * max_cross_product

