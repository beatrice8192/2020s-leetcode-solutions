# https://leetcode.com/problems/implement-queue-using-stacks
from collections import deque

class MyQueue(object):

    def __init__(self):
        self.stackTopDown = deque()
        self.stackBottomUp = deque()
        self.front = None

    # O(n)
    def push(self, x: int) -> None:
        while (len(self.stackTopDown) > 0):
            self.stackBottomUp.append(self.stackTopDown.pop());

        if (len(self.stackBottomUp) == 0):
            self.front = x
        self.stackBottomUp.append(x)

    # O(n)
    def pop(self) -> int:
        while (len(self.stackBottomUp) > 0):
            self.stackTopDown.append(self.stackBottomUp.pop())

        x = self.stackTopDown.pop()
        if (len(self.stackTopDown) > 0):
            self.front = self.stackTopDown.pop()
            self.stackTopDown.append(self.front)
        return x

    # O(1)
    def peek(self) -> int:
        return self.front

    # O(1)
    def empty(self) -> bool:
        return (len(self.stackTopDown) == 0) and (len(self.stackBottomUp) == 0)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

