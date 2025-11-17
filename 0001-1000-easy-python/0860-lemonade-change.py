# https://leetcode.com/problems/lemonade-change
class Solution(object):
    # def lemonadeChange(self, bills: List[int]) -> bool:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = 0
        tens = 0
        # no need to keep track of twenties
        for b in bills:
            if (b == 5):
                fives += 1
            elif (b == 10):
                tens += 1
                if (fives == 0):
                    return False
                else:
                    fives -= 1
            elif (b == 20):
                if (fives == 0):
                    return False
                else:
                    if (tens > 0):
                        fives -= 1
                        tens -= 1
                    elif (fives >= 3):
                        fives -= 3
                    else:
                        return False
        return True

