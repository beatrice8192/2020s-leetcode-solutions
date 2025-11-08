# https://leetcode.com/problems/binary-search
class Solution(object):
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while (start + 1 < end):
            mid = int((start + end) / 2)
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                end = mid
            else:
                start = mid
        return start if (nums[start] == target) else -1

