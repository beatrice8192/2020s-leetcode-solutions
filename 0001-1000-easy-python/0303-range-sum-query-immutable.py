# https://leetcode.com/problems/range-sum-query-immutable
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sums[right] - (0 if left == 0 else self.sums[left - 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

