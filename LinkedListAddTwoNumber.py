# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + ('' if not self.next else '->' + str(self.next) )


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carriage = ListNode()
        
        a = l1
        b = l2
        result = ListNode()
        pre = result
        while a or b:
            if not a:
                c = b if not carriage else ListNode(carriage.val + b.val)
                b = b.next
            elif not b:
                c = a if not carriage else ListNode(carriage.val + a.val)
                a = a.next
            else:
                c = ListNode(a.val + b.val) if not carriage else ListNode(a.val + b.val + carriage.val)
                a = a.next
                b = b.next
            carriage.val = c.val // 10
            c.val = c.val % 10
            pre.next = c
            pre = c
        if carriage.val > 0:
            pre.next = carriage
        return result.next
        



s = Solution()
print(s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
print(s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))