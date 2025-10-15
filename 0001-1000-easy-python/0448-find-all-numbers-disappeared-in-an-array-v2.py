# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
class Solution(object):
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while (nums[i] != nums[nums[i] - 1]):
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        return [i + 1 for i in range(len(nums)) if i != nums[i] - 1]

