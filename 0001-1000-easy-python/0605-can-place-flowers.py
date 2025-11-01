# https://leetcode.com/problems/can-place-flowers
class Solution(object):
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        last_one = -1
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 1):
                if (last_one == -1):
                    count += int((i - last_one - 1) / 2)
                else:
                    count += int((i - last_one - 2) / 2)
                last_one = i
        if (last_one == -1):
            count += int((len(flowerbed) - last_one) / 2)
        else:
            count += int((len(flowerbed) - last_one - 1) / 2)
        return count >= n

