# https://leetcode.com/problems/island-perimeter
class Solution(object):
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (grid[r][c] == 1):
                    result += 4
                    if (c > 0 and grid[r][c-1] == 1):
                        result -= 2
                    if (r > 0 and grid[r-1][c] == 1):
                        result -= 2
        return result

