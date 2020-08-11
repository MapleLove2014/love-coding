# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        store = head
        count = 0
        # compute size
        while head:
            count += 1
            head = head.next
        head = store

        if count == n:
            return store.next

        # skip count - n nodes
        skips = 0

        while head and skips < count - n - 1:
            skips += 1
            head = head.next
        nthNode = head.next
        head.next = nthNode.next
        return store 
    
    def onePass(self, head, n):
        store = head
        first = head
        second = head
        count = 0
        while second and count < n + 1:
            count += 1
            second = second.next
        if not second and count < n + 1 :
            return store.next
        while second:
            second = second.next
            first = first.next
        first.next = first.next.next
        return store