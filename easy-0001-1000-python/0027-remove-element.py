# https://leetcode.com/problems/remove-element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for item in nums:
            if item != val:
                nums[i] = item
                i += 1
        return i

