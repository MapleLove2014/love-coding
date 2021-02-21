# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dedupHead = head if head.val != head.next.val else None
        preNode = dedupHead
        while head:
            node = self.skipDuplicateNodes(head)
            if not node:
                break
            if not dedupHead:
                dedupHead = node
                preNode = node
            else:
                preNode.next = node
                preNode = node
            head = node
        if preNode:
            preNode.next = None
        return dedupHead

    def skipDuplicateNodes(self, head):
        node = head.next
        value = head.val
        while node:
            if node.val != value and (not node.next or node.val != node.next.val):
                return node
            value = node.val
            node = node.next
        return node

s = Solution()
s.deleteDuplicates(ListNode(1, ListNode(2, ListNode(2))))
s.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))))