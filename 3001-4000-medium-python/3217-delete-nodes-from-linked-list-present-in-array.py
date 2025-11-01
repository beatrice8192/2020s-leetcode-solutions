# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        new_head = head
        while (new_head != None and new_head.val in nums):
            new_head = new_head.next
        node = new_head
        while (node != None):
            while (node.next and node.next.val in nums):
                node.next = node.next.next
            node = node.next
        return new_head

