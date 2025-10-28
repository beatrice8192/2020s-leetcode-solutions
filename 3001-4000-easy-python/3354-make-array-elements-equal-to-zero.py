# https://leetcode.com/problems/make-array-elements-equal-to-zero
class Solution(object):
    # def countValidSelections(self, nums: List[int]) -> int:
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            left_sum += nums[i]
            if (left_sum * 2 < total_sum - 1):
                continue
            elif (left_sum * 2 > total_sum + 1):
                break
            elif (nums[i] == 0):
                count += 2 if (left_sum * 2 == total_sum) else 1
        return count

