# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        node = head
        while node:
            nextNode = node.next
            node.next = newHead
            newHead = node
            node = nextNode
        return newHead