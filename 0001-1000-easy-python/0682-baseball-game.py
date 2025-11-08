# https://leetcode.com/problems/baseball-game
class Solution(object):
    # def calPoints(self, operations: List[str]) -> int:
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        array = []
        for o in operations:
            if (o == "+"):
                array.append(array[-1] + array[-2])
            elif (o == "D"):
                array.append(array[-1] * 2)
            elif (o == "C"):
                array.pop()
            else:
                array.append(int(o))
        return sum(array)

