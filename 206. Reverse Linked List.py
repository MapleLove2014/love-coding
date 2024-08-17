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
    
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, None)
        n = head
        while n:
            newHead = d.next
            nn = n.next
            n.next = newHead
            d.next = n
            n = nn
        return d.next
    