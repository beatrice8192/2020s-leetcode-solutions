# https://leetcode.com/problems/container-with-most-water
class Solution(object):
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        start = 0
        end = len(height) - 1
        while (start < end):
            area = min(height[start], height[end]) * (end - start)
            result = max(result, area)
            if (height[start] < height[end]):
                start += 1
            else:
                end -= 1
        return result

