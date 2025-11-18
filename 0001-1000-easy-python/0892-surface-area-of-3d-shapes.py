# https://leetcode.com/problems/surface-area-of-3d-shapes
class Solution(object):
    # def surfaceArea(self, grid: List[List[int]]) -> int:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        result = sum([1 for row in grid for cell in row if cell > 0]) * 2
        for r in range(rows):
            for c in range(columns):
                result += grid[r][c] * 4
                if (r > 0):
                    result -= min(grid[r][c], grid[r-1][c]) * 2
                if (c > 0):
                    result -= min(grid[r][c], grid[r][c-1]) * 2
        return result

