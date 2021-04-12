# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = head
        shead = None
        dummy = ListNode(0, head)
        while node:
            nodeNext = node.next
            if not shead:
                shead = node
                shead.next = None
            else:
                dummy = ListNode(0, shead)
                pnode = dummy
                snode = shead
                while snode:
                    if node.val < snode.val:
                        pnode.next = node
                        node.next = snode
                        break
                    pnode = snode
                    snode = snode.next
                if not snode and node.val >= pnode.val:
                    pnode.next = node
                    node.next = None
                shead = dummy.next
            node = nodeNext
        return dummy.next


