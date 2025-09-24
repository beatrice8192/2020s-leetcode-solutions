# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while (node != None):
            if (node.next != None and node.val == node.next.val):
                node.next = node.next.next
            else:
                node = node.next
        return head

