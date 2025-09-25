# https://leetcode.com/problems/plus-one
class Solution(object):
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            carry += digits[i]
            digits[i] = carry % 10
            carry = int(carry / 10)
        if (carry == 1):
            digits.insert(0, 1)
        return digits

