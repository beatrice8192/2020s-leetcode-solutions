# https://leetcode.com/problems/valid-parentheses
class Solution(object):
    # def isValid(self, s: str) -> bool:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = set(['(', '[', '{'])
        closing = set([')', ']', '}'])
        matches = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if (char in opening):
                stack.append(char)
            elif (char in closing):
                if (len(stack) > 0 and stack[-1] == matches[char]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

