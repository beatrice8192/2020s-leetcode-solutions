# https://leetcode.com/problems/implement-stack-using-queues
from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        self.front = None

    # O(n)
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (self.front != None):
            self.queue.appendleft(self.front)
            for i in range(len(self.queue) - 1):
                self.queue.appendleft(self.queue.pop())
        self.front = x

    # O(1)
    def pop(self):
        """
        :rtype: int
        """
        tmp = self.front
        if len(self.queue) == 0:
            self.front = None
        else:
            self.front = self.queue.pop()
        return tmp

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
        return len(self.queue) == 0 and self.front == None

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

