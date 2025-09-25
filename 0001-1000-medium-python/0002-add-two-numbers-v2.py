# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# modify l1 in-place
class Solution(object):
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = l1
        tail = None
        carry = 0
        while (l1 != None):
            carry += l1.val
            carry += l2.val if (l2 != None) else 0
            l1.val = carry % 10
            carry = int(carry / 10)
            if (l1.next == None):
                tail = l1
            l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        tail.next = l2
        while (l2 != None and carry != 0):
            carry += l2.val
            l2.val = carry % 10
            carry = int(carry / 10)
            if (l2.next == None):
                tail = l2
            l2 = l2.next
        if (carry != 0):
            tail.next = ListNode(carry)
        return head

