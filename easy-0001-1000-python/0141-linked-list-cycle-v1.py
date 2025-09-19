# https://leetcode.com/problems/linked-list-cycle
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # reverse linked list
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None or head.next == None):
            return False
        last2 = None
        last1 = head
        node = head.next
        while (node != None):
            if (node == head):
                return True
            last1.next = last2
            last2 = last1
            last1 = node
            node = node.next
        return False

