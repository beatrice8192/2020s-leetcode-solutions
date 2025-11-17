# https://leetcode.com/problems/buddy-strings
class Solution(object):
    # def buddyStrings(self, s: str, goal: str) -> bool:
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if (len(s) != len(goal)):
            return False
        elif (s == goal):
            l = list(s)
            return len(l) > len(set(l)) # contains duplicates
        start = 0
        end = len(s) - 1
        while (start < len(s) and s[start] == goal[start]):
            start += 1
        while (end > start and s[end] == goal[end]):
            end -= 1
        return s[start] == goal[end] and s[end] == goal[start] and s[start+1:end] == goal[start+1:end]

