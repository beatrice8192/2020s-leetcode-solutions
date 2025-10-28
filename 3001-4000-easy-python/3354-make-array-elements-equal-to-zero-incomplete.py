# https://leetcode.com/problems/make-array-elements-equal-to-zero
class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        left_sum = 0
        right_sum = 0
        remainder = sum(nums)
        while (left <= right and remainder > 1 and left < len(nums) and right >= 0):
            if (left_sum < right_sum):
                left_sum += nums[left]
                remainder -= nums[left]
                left += 1
            else:
                right_sum += nums[right]
                remainder -= nums[right]
                right -= 1
        print(left, right, left_sum, right_sum, remainder)
        diff = abs(left_sum - right_sum)
        if (abs(diff - remainder) > 1):
            return 0
        else:
            count = nums[left:(right+1)].count(0)
            if (abs(diff - remainder) == 1):
                return count
            elif (diff == 0 and remainder == 0):
                return count * 2
        count = 0
        while (left <= right and remainder > 0 and left < len(nums) and right >= 0):
            if (left_sum < right_sum):
                if (nums[left] == 0):
                    count += 1
                left_sum += nums[left]
                remainder -= nums[left]
                left += 1
            else:
                if (nums[right] == 0):
                    count += 1
                right_sum += nums[right]
                remainder -= nums[right]
                right -= 1
        print(left, right, left_sum, right_sum, remainder, count)
        return count + nums[left:(right+1)].count(0) * 2

