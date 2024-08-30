# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n <= 1:
            return True
        ha = n // 2
        firstHalf = None
        node = head
        while ha > 0:
            tmp = node.next
            node.next = firstHalf
            firstHalf = node
            node = tmp
            ha -= 1
        secondHalf = node if n % 2 == 0 else node.next
        while firstHalf and secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True if not firstHalf and not secondHalf else False
    
s = Solution()
print(s.isPalindrome(ListNode(0, ListNode(0))))
print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))

