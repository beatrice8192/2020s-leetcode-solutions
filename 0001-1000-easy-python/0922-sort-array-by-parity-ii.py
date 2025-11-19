# https://leetcode.com/problems/sort-array-by-parity-ii
class Solution(object):
    # def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = 0
        for left in range(len(nums)):
            if ((nums[left] - left) & 1 == 1):
                right = max(right, left)
                while (right < len(nums) and not ((nums[right] - right) & 1 == 1 and (nums[right] - left) & 1 == 0)):
                    right += 1
                nums[left], nums[right] = nums[right], nums[left]
        return nums

