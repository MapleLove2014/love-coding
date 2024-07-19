# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
class Solution:
    def deleteDuplicates(self, head):
        d = ListNode(-2**31, head)
        last = d
        node = head
        while node:
            start=node.next
            count = 1
            while start and start.val == node.val:
                count += 1
                start = start.next
            if count > 1:
                node = start
                continue
            last.next = node
            last = last.next
            node = start
        last.next = None
        return d.next

s = Solution()
print(s.deleteDuplicates(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, None))))))))

        