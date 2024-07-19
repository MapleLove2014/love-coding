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
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(-2**31, head)
        last=d
        node=head
        while node:
            if node.val != last.val:
                last.next = node
                last= last.next
            node = node.next
        last.next = None
        return d.next
