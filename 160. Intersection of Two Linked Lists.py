# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB
        while h1 != h2:
            h1 = h1.next if h1 else headB
            h2 = h2.next if h2 else headA

        return h1

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode):
        d1 = ListNode(2**31, headA)
        d2 = ListNode(-2**31, headB)

        def size(head):
            l = 0
            while head:
                l += 1
                head = head.next
        def jump(head, n):
            while n > 0:
                n -= 1
                head = head.next
            return head
        l1 = size(d1)
        l2 = size(d2)

        if l1 >= l2:
            d1 = jump(d1, l1 - l2)
        else:
            d2 = jump(d2, l2 - l1)
        while d1 and d2:
            if d1.val == d2.val:
                return d1
            d1 = d1.next
            d2 = d2.next
        return None


