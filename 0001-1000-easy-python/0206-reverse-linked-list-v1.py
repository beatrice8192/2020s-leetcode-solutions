# https://leetcode.com/problems/reverse-linked-list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # step 1: {last2} -> {last1} -> {next1} -> {next2}
    # step 2: {last2} <- {last1}    {next1} -> {next2}
    # step 3: {     } <- {last2}    {last1} -> {next1}

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        last2 = None
        last1 = head
        while (last1 != None):
            next1 = last1.next
            last1.next = last2
            last2 = last1
            last1 = next1
        return last2

