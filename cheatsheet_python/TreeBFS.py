class TreeBFS:
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
            self.index = self.bfs_start
            self.level += 1
        return self.bfs_start < self.bfs_end

    def getNext(self):
        top = self.bfs_queue[self.index]
        self.bfs_queue.extend(self.get_children(top))
        self.index += 1
        return top

