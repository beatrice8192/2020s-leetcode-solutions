# https://leetcode.com/problems/flipping-an-image
class Solution(object):
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i] = list(reversed([1 - x for x in image[i]]))
        return image

