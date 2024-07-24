# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = ListNode(0, head)
        t = d
        h = d
        while True:
            for _ in range(2):
                if not h.next:
                    return False
                h = h.next
            if not t.next:
                return False
            t = t.next
            if t == h:
                return True
        

