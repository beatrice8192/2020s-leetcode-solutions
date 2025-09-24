# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = ListNode()
        node = list3
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        if (list1 != None):
            node.next = list1
        if (list2 != None):
            node.next = list2
        return list3.next

