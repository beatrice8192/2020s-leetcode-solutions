# https://leetcode.com/problems/count-unguarded-cells-in-the-grid
class Solution(object):
    # def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [["" for c in range(n)] for r in range(m)]
        def occupied(r, c):
            return grid[r][c] == "G" or grid[r][c] == "W"
        for w in walls:
            grid[w[0]][w[1]] = "W"
        for g in guards:
            grid[g[0]][g[1]] = "G"
        for g in guards:
            r = g[0] - 1
            while (r >= 0 and not occupied(r, g[1])):
                grid[r][g[1]] = "g"
                r -= 1
            r = g[0] + 1
            while (r < m and not occupied(r, g[1])):
                grid[r][g[1]] = "g"
                r += 1
            c = g[1] - 1
            while (c >= 0 and not occupied(g[0], c)):
                grid[g[0]][c] = "g"
                c -= 1
            c = g[1] + 1
            while (c < n and not occupied(g[0], c)):
                grid[g[0]][c] = "g"
                c += 1
        return len([cell for row in grid for cell in row if cell == ""])

