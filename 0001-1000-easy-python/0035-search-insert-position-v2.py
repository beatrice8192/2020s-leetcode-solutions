# https://leetcode.com/problems/search-insert-position
class Solution(object):
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while (start < end):
            if (target <= nums[start]):
                return start
            elif (start + 1 >= end):
                return end 
            mid = int((start + end) / 2)
            if (target < nums[mid]):
                end = mid
            else:
                start = mid
        return -1

