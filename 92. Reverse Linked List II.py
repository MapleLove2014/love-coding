# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head:
            return head
        node = head
        l1=None
        l = node
        r = node
        while node and (left >= 1 or right >= 1):
            if left == 2:
                l1 = node
            if left == 1:
                l = node
            if right == 1:
                r = node
            left -= 1
            right -= 1
            node = node.next
        rh = r.next
        for _ in range(-1, right - left):
            temp = l.next
            l.next = rh
            rh = l
            l = temp
        if not l1:
            return rh
        l1.next = rh
        return head
    
    def reverseBetween2(self, head, left: int, right: int):
        if not head or not head.next:
            return head
        d = ListNode(0, head)
        l = d
        node = head
        while left > 1 and node:
            l = node
            left -= 1
            right -= 1
            node = node.next
        nt = node
        l.next = None
        for _ in range(-1, right - left):
            # l -> node
            t = node.next
            node.next = l.next
            l.next = node
            node = t
        nt.next = node
        return d.next

def g(l, r):
    t = ListNode(0)
    n = t
    for i in range(l, r+1):
        n.next = ListNode(i)
        n = n.next
    return t.next


s = Solution()
print(s.reverseBetween2(g(1,5), 2, 4))
print(s.reverseBetween2(g(5, 5), 1, 1))
print(s.reverseBetween2(g(4,5), 1, 2))
