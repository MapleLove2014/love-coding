# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + '->' + str(self.next)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length <= 2:
            return
        mid = length // 2

        node = head
        i = 0
        while i < mid:
            node = node.next
            i += 1

        rightHalfHead = node if length % 2 == 0 else node.next

        def reverse(head):
            prevHead = None

            node = head
            while node:
                nodeNext = node.next
                node.next = prevHead
                prevHead = node
                node = nodeNext
            return prevHead
        rightHalfHead = reverse(rightHalfHead)

        left = head
        right = rightHalfHead
        while left and right:
            leftNext = left.next
            rightNext = right.next
            left.next = right
            right.next = leftNext
            left = leftNext
            right = rightNext
        left.next = None
        print(head)

    def reorderList2(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d = ListNode(0, head)
        node = d.next
        l = 0
        while node:
            l += 1
            node = node.next
        
        skip = l // 2 + (l % 2)
        node = d.next
        while skip > 0:
            skip -= 1
            if skip == 0:
                nn = node.next
                node.next = None
                node = nn
            else:
                node = node.next
        rh = None
        while node:
            n = node.next 
            node.next = rh
            rh = node
            node = n
        ops = l // 2
        node = d.next
        while node and rh and ops > 0:
            n = node.next
            node.next = rh
            rn = rh.next
            rh.next = n
            rh = rn
            node = n
            ops -= 1
        return d.next

s = Solution()
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))