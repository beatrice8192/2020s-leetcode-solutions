# https://leetcode.com/problems/linked-list-cycle
# referencing the solution of:
# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# reverse linked list
class Solution(object):
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None or head.next == None):
            return False
        else:
            return (head == self.reverseList(head))

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

