# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return str(self.val) + "->" + str(self.next)
class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next or k == 0:
            return head
        
        size=0
        node=head
        while node:
            size += 1
            node = node.next
        forward=size - (k % size)
        if forward == size:
            return head
        node = head
        while forward > 1:
            node = node.next
            forward -= 1
        newhead=node.next
        node.next=None
        newtail=newhead
        while newtail.next:
            newtail =newtail.next
        newtail.next = head
        return newhead
        



        


    

# d->0->1->2  4
# d->1->2->3->4->5->6  2
        

s=Solution()
print(s.rotateRight(ListNode(1, ListNode(2, None)), 2))
print(s.rotateRight(ListNode(1, ListNode(2, None)), 1))
print(s.rotateRight(ListNode(1, ListNode(2, ListNode(3, None))), 4))
print(s.rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, None))))), 2))









