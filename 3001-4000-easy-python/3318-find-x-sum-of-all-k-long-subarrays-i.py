# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i
class Solution(object):
    # def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        answer = [0] * (len(nums) - (k - 1))
        occurrences = {}
        def increment(n):
            if (n not in occurrences):
                occurrences[n] = 0
            occurrences[n] += 1
        def decrement(n):
            occurrences[n] -= 1
        for i in range(k - 1):
            increment(nums[i])
        for i in range(len(nums) - (k - 1)):
            increment(nums[i + (k - 1)])
            frequencies = list(reversed(sorted([(occurrences[n], n) for n in occurrences])))
            for j in range(min(x, len(frequencies))):
                answer[i] += frequencies[j][0] * frequencies[j][1]
            decrement(nums[i])
        return answer

