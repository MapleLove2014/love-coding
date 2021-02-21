# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        listAfterPair = head.next.next
        head.next.next = head
        reverseHead = head.next
        head.next = self.swapPairs(listAfterPair)
        return reverseHead