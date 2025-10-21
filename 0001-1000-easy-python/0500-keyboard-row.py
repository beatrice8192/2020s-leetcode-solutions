# https://leetcode.com/problems/keyboard-row
class Solution(object):
    # def findWords(self, words: List[str]) -> List[str]:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [{
            'q': None, 'w': None, 'e': None, 'r': None,
            't': None, 'y': None, 'u': None, 'i': None, 'o': None, 'p': None
        }, {
            'a': None, 's': None, 'd': None, 'f': None,
            'g': None, 'h': None, 'j': None, 'k': None, 'l': None
        }, {
            'z': None, 'x': None, 'c': None, 'v': None,
            'b': None, 'n': None, 'm': None
        }]
        def test(word):
            for row in rows:
                if (len(word) == len([char for char in word if lower(char) in row])):
                    return True
        return [word for word in words if test(word)]

