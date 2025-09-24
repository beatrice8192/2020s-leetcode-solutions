# https://leetcode.com/problems/valid-parentheses
class Solution(object):
    OPENING = ['(', '[', '{']
    CLOSING = [')', ']', '}']
    MATCHES = {')':'(', ']':'[', '}':'{'}

    # def isValid(self, s: str) -> bool:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if (char in self.OPENING):
                stack.append(char)
            elif (char in self.CLOSING):
                if (len(stack) > 0 and stack[-1] == self.MATCHES[char]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

