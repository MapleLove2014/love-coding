# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + "->" + str(self.next) 
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        def reverse(begin, nodes):
            a = begin
            rh = None
            last = None
            while a and nodes > 0:
                temp = a.next
                a.next = rh
                rh = a
                a = temp
                last = a
                nodes -= 1
            begin.next = last
            return rh

        dummy = ListNode(0, head)

        prev = dummy
        count = left
        while count > 1 and prev:
            prev = prev.next
            count -= 1
        if not prev or not prev.next :
            return dummy.next
        
        prev.next = reverse(prev.next, right - left + 1)

        return dummy.next

s = Solution()
print(s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4))
