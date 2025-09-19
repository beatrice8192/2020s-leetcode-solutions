# https://leetcode.com/problems/linked-list-cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # Floyd's Cycle-Finding Algorithm
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None or head.next == None):
            return False
        slow = head
        fast = head.next
        while (True):
            if (slow == fast):
                return True
            if (slow.next != None):
                slow = slow.next
            else:
                break
            if (fast.next != None and fast.next.next != None):
                fast = fast.next.next
            else:
                break
        return False

