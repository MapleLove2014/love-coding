# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        dummy = head
        node = head
        while node:
            next = node.next
            if previous and previous.val == node.val:
                previous.next = next
                node.next = None
            else:
                previous = node
            node = next
        return dummy
