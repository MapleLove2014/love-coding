# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + '->' + str(self.next)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        dummy = ListNode()
        node = dummy
        while l1 or l2 or carry > 0:
            part1 = l1.val if l1 else 0
            part2 = l2.val if l2 else 0
            s = part1 + part2 + carry
            carry = s // 10
            left = s % 10

            node.next = ListNode(left)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.reverse(dummy.next)

    def reverse(self, list: ListNode) -> ListNode:
        node = list
        newHead = None
        while node:
            nodeNext = node.next
            node.next = newHead
            newHead = node
            node = nodeNext
        return newHead


    def solu2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        def listSum(list: Optional[ListNode]):
            node = list
            s = 0
            while node:
                s *= 10
                s += node.val
                node = node.next

            return s
        s = listSum(l1) + listSum(l2)
        node = None

        while s > 0:
            newNode = ListNode(s % 10)
            newNode.next = node
            node = newNode
            s = s // 10
        
        return node if node else ListNode(0)


        
s = Solution()
r = s.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4))))
print(r)

print(s.addTwoNumbers(ListNode(5), ListNode(5)))


print(s.solu2(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4)))))
print(s.solu2(ListNode(5), ListNode(5)))
