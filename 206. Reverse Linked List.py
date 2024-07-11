# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        node = head
        while node:
            nextNode = node.next
            node.next = newHead
            newHead = node
            node = nextNode
        return newHead

    def reverseList(self, head):
        def reverse(head):
            if not head or not head.next:
                return head
            p = reverse(head.next)
            head.next.next = head
            head.next = None
            return p
        return reverse(head)
    