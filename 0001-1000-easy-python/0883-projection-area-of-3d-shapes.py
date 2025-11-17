# https://leetcode.com/problems/projection-area-of-3d-shapes
class Solution(object):
    # def projectionArea(self, grid: List[List[int]]) -> int:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy = sum([1 for x in grid for cell in x if cell > 0])
        xz = sum([max(x) for x in grid])
        yz = sum([max([x[i] for x in grid]) for i in range(len(grid[0]))])
        return xy + xz + yz

