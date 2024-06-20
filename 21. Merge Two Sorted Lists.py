from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        head=dummy
        i=list1
        j=list2
        while i and j:
            if i.val <= j.val:
                head.next=i
                head=head.next
                i=i.next
            else:
                head.next=j
                head=head.next
                j=j.next
        k=i if i else j
        while k:
            head.next=k
            head=head.next
            k=k.next
        return dummy.next        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        head = None
        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                if tail:
                    tail.next = list1
                tail = list1
                list1 = temp
            else:
                temp = list2.next
                if tail:
                    tail.next = list2
                tail = list2
                list2 = temp
            if not head:
                head = tail
            tail.next = None
        if list1:
            if not tail:
                return list1
            tail.next = list1
        if list2:
            if not tail:
                return list2
            tail.next = list2
        return head

