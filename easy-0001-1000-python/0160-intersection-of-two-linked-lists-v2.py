# https://leetcode.com/problems/intersection-of-two-linked-lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # two pointers
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        while (nodeA != nodeB):
            if (nodeA == None):
                nodeA = headB
            else:
                nodeA = nodeA.next
            if (nodeB == None):
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA

