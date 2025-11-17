# https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head # 1 step per turn
        fast = head # 2 steps per turn
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next
            if (fast != None):
                fast = fast.next
        return slow

