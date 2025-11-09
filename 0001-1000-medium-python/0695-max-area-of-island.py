# https://leetcode.com/problems/max-area-of-island
class Solution(object):
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        rows = len(grid)
        columns = len(grid[0])
        def visited(r, c):
            return grid[r][c] != 1
        def set_visited(r, c):
            grid[r][c] = 2
        def get_children(node):
            return BFS.matrixGetChildren(node, rows, columns, visited, set_visited)
        for r in range(rows):
            for c in range(columns):
                if visited(r, c):
                    continue
                bfs = BFS((r, c), get_children)
                while bfs.hasNext():
                    node = bfs.getNext()
                result = max(result, len(set(bfs.bfs_queue)))
        return result

class BFS:
    def __init__(self, root, get_children):
        self.get_children = get_children
        self.bfs_queue = [root]
        self.bfs_start = 0
        self.bfs_end = len(self.bfs_queue)
        self.index = 0
        self.level = 0

    def hasNext(self):
        if (self.index == self.bfs_end):
            self.bfs_start = self.bfs_end
            self.bfs_end = len(self.bfs_queue)
            self.level += 1
        return self.bfs_start < self.bfs_end

    def getNext(self):
        node = self.bfs_queue[self.index]
        self.bfs_queue.extend(self.get_children(node))
        self.index += 1
        return node

    @staticmethod
    def matrixGetChildren(node, rows, columns, visited, set_visited):
        r = node[0]
        c = node[1]
        if (visited(r, c)):
            return []
        set_visited(r, c)
        children = []
        if (r-1 >= 0 and not visited(r-1, c)):
            children.append((r-1, c))
        if (r+1 < rows and not visited(r+1, c)):
            children.append((r+1, c))
        if (c-1 >= 0 and not visited(r, c-1)):
            children.append((r, c-1))
        if (c+1 < columns and not visited(r, c+1)):
            children.append((r, c+1))
        return children

