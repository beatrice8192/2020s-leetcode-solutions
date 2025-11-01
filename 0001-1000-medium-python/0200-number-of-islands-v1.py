# https://leetcode.com/problems/number-of-islands
class Solution(object):
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if (grid[i][j] != "1"):
                    continue
                count += 1
                bfs_queue = [(i, j)]
                bfs_start = 0
                bfs_end = len(bfs_queue)
                while (bfs_start < bfs_end):
                    for k in range(bfs_start, bfs_end):
                        r = bfs_queue[k][0]
                        c = bfs_queue[k][1]
                        if (grid[r][c] != "1"):
                            continue
                        grid[r][c] = "2"
                        if (r-1 >= 0 and grid[r-1][c] == "1"):
                            bfs_queue.append((r-1, c))
                        if (r+1 < rows and grid[r+1][c] == "1"):
                            bfs_queue.append((r+1, c))
                        if (c-1 >= 0 and grid[r][c-1] == "1"):
                            bfs_queue.append((r, c-1))
                        if (c+1 < columns and grid[r][c+1] == "1"):
                            bfs_queue.append((r, c+1))
                    bfs_start = bfs_end
                    bfs_end = len(bfs_queue)
        return count

