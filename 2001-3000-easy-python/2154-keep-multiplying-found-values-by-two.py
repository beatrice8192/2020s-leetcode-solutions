# https://leetcode.com/problems/keep-multiplying-found-values-by-two
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while True:
            if (original not in nums):
                return original
            else:
                original *= 2
        return original

