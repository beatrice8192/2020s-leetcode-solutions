# https://leetcode.com/problems/minimum-index-sum-of-two-lists
class Solution(object):
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        min_sum = sys.maxsize
        map1 = {list1[i]: i for i in range(len(list1))}
        map2 = {list2[i]: i for i in range(len(list2))}
        for key in map1:
            if key in map2:
                key_sum = map1[key] + map2[key]
                if (key_sum < min_sum):
                    min_sum = key_sum
                    result = [key]
                elif (key_sum == min_sum):
                    result.append(key)
        return result

