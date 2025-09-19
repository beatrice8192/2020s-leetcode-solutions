# https://leetcode.com/problems/intersection-of-two-linked-lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # stack
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stackA = []
        stackB = []
        while (headA != None):
            stackA.append(headA)
            headA = headA.next
        while (headB != None):
            stackB.append(headB)
            headB = headB.next
        intersect = None
        while (len(stackA) > 0 and len(stackB) > 0 and stackA[-1] == stackB[-1]):
            intersect = stackA[-1]
            del stackA[-1]
            del stackB[-1]
        return intersect

