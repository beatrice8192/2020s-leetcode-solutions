# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for item in nums:
            if nums[i] != item:
                i += 1
                nums[i] = item
        return i + 1

