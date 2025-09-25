# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# two pointers
class Solution(object):
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 1
        count = 1
        for fast in range(1, len(nums)):
            if (nums[fast] == nums[fast - 1]):
                count += 1
                if (count <= 2):
                    nums[slow] = nums[fast]
                    slow += 1
                    # else: count > 2, slow stays unchanged, fast keeps moving
            else:
                count = 1
                nums[slow] = nums[fast]
                slow += 1
        return slow

