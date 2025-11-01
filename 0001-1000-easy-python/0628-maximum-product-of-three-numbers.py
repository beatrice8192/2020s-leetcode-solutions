# https://leetcode.com/problems/maximum-product-of-three-numbers
class Solution(object):
    # def maximumProduct(self, nums: List[int]) -> int:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        product1 = reduce(lambda x, y: x * y, nums[-3:])
        product2 = reduce(lambda x, y: x * y, nums[:2]) * nums[-1]
        return max(product1, product2)

