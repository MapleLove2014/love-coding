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

    def insertionSortList2(self, head):
        d = ListNode(-2**31, None)
        p = head
        lastP = None
        while p:
            node = d if not lastP or lastP.val >= p.val else lastP # do not need to check from head each time
            while node and node.val < p.val:
                if not node.next or node.next.val >= p.val:
                    break
                node = node.next
            nn = node.next
            node.next = p
            pn = p.next
            p.next = nn
            lastP = p
            p = pn
        return d.next


