# https://leetcode.com/problems/plus-one
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            value = digits[i] + carry
            carry = value / 10
            digits[i] = value % 10
        if carry == 1:
            digits.insert(0, 1)
        return digits

