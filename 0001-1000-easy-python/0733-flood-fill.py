# https://leetcode.com/problems/flood-fill
class Solution(object):
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        columns = len(image[0])
        old_color = image[sr][sc]
        def visited(r, c):
            return image[r][c] == color or image[r][c] != old_color
        def set_visited(r, c):
            image[r][c] = color
        def get_children(node):
            return BFS.matrixGetChildren(node, rows, columns, visited, set_visited)
        bfs = BFS((sr, sc), get_children)
        while bfs.hasNext():
            node = bfs.getNext()
        return image

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

