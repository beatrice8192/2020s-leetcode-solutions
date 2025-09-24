# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.recursion(head)[0]

    # return (new_head, new_tail)
    def recursion(self, head):
        if head == None or head.next == None:
            # 0 or 1 elements
            return (head, head)
        else:
            # 2 or more elements
            reverse = self.recursion(head.next)
            reverse[1].next = head
            head.next = None
            return (reverse[0], head)

