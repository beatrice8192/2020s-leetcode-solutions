# https://leetcode.com/problems/robot-return-to-origin
class Solution(object):
    # def judgeCircle(self, moves: str) -> bool:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        commands = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}
        return sum([commands[x][0] for x in moves]) == 0 and sum([commands[x][1] for x in moves]) == 0

