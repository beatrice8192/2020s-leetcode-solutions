# https://leetcode.com/problems/unique-morse-code-words
class Solution(object):
    # def uniqueMorseRepresentations(self, words: List[str]) -> int:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set(["".join([morse[ord(char) - 97] for char in word]) for word in words]))

