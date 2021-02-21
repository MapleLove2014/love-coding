# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k:
            return head
        count = self.listSize(head)
        endAt = count - (k % count)
        if endAt == count:
            return head
        endNode = self.nodeAt(head, endAt)
        lastNode = self.nodeAt(endNode.next, count - endAt)
        return self.rotate(head, lastNode, endNode)

    def rotate(self, head, lastNode, endNode):
        lastNode.next = head
        rotateListHead = endNode.next
        endNode.next = None
        return rotateListHead

    def nodeAt(self, head, i):
        node = None
        while i > 0:
            node = head
            head = head.next
            i -= 1
        return node

    def listSize(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
s.rotateRight(head, 2)

