# https://leetcode.com/problems/1-bit-and-2-bit-characters
class Solution(object):
    # def isOneBitCharacter(self, bits: List[int]) -> bool:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        last_bit = False
        while (i < len(bits)):
            if (bits[i] == 0):
                i += 1
                last_bit = True
            else:
                i += 2
                last_bit = False
        return last_bit

