# https://leetcode.com/problems/implement-stack-using-queues
from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        self.front = None

    # O(1)
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.appendleft(x)
        self.front = x

    # O(n)
    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue) - 1):
            self.front = self.queue.pop()
            self.queue.appendleft(self.front)
        return self.queue.pop()

    # O(1)
    def top(self):
        """
        :rtype: int
        """
        return self.front

    # O(1)
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
