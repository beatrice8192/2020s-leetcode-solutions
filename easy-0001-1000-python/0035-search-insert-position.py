# https://leetcode.com/problems/search-insert-position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bisect(nums, target, 0, len(nums))

    def bisect(self, nums, target, start, end):
        if target <= nums[start]:
            return start
        elif start + 1 >= end:
            return end
        mid = (start + end) / 2
        if target < nums[mid]:
            return self.bisect(nums, target, start, mid)
        else:
            return self.bisect(nums, target, mid, end)

