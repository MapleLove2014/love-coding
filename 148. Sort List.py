# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        def sort(head, length):
            if not head or length <= 1:
                return head
            mid = length // 2
            node = head
            prev = None
            count = 0
            while count < mid:
                prev = node
                node = node.next
                count += 1
            prev.next = None
            left = sort(head, length // 2 )
            right = sort(node, length - length // 2)
            dummy = ListNode()
            prev = dummy
            lnode = left
            rnode = right
            while True:  
                if lnode and rnode:
                    if lnode.val <= rnode.val:
                        lnext = lnode.next
                        prev.next = lnode
                        lnode.next = None
                        lnode = lnext
                        prev = prev.next
                    else:
                        rnext = rnode.next
                        prev.next = rnode
                        rnode.next = None
                        rnode = rnext
                        prev = prev.next
                elif lnode:
                    lnext = lnode.next
                    prev.next = lnode
                    lnode.next = None
                    lnode = lnext
                    prev = prev.next
                elif rnode:
                    rnext = rnode.next
                    prev.next = rnode
                    rnode.next = None
                    rnode = rnext
                    prev = prev.next
                else:
                    return dummy.next
        return sort(head, length)
