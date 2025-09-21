# https://leetcode.com/problems/remove-linked-list-elements
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while (head != None and head.val == val):
            head = head.next
        node = head
        while (node != None):
            while (node.next != None and node.next.val == val):
                node.next = node.next.next
            node = node.next
        return head

