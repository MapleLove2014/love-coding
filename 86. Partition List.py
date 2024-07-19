# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        low=ListNode(0, None)
        lowh=low
        high=ListNode(0, None)
        highh=high
        node=head
        while node:
            if node.val < x:
                low.next = node
                low=low.next
            else:
                high.next = node
                high=high.next
            node = node.next
        high.next=None
        low.next=highh.next
        return lowh.next
        
# [1,4,3,2,5,2]
# 1 2 2 