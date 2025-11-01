# https://leetcode.com/problems/count-sub-islands
class Solution(object):
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid2)
        columns = len(grid2[0])
        for i in range(rows):
            for j in range(columns):
                if (grid2[i][j] != 1):
                    continue
                out_of_bound = False
                bfs_queue = [(i, j)]
                bfs_start = 0
                bfs_end = len(bfs_queue)
                while (bfs_start < bfs_end):
                    for k in range(bfs_start, bfs_end):
                        r = bfs_queue[k][0]
                        c = bfs_queue[k][1]
                        if (grid2[r][c] != 1):
                            continue
                        elif (grid1[r][c] != 1):
                            out_of_bound = True
                        grid2[r][c] = 2
                        if (r-1 >= 0 and grid2[r-1][c] == 1):
                            bfs_queue.append((r-1, c))
                        if (r+1 < rows and grid2[r+1][c] == 1):
                            bfs_queue.append((r+1, c))
                        if (c-1 >= 0 and grid2[r][c-1] == 1):
                            bfs_queue.append((r, c-1))
                        if (c+1 < columns and grid2[r][c+1] == 1):
                            bfs_queue.append((r, c+1))
                    bfs_start = bfs_end
                    bfs_end = len(bfs_queue)
                if (not out_of_bound):
                    count += 1
        return count

