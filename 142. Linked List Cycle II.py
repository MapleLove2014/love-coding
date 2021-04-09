# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        node = head
        while node:
            if node in nodes:
                return node
            nodes.add(node)
            node = node.next
        return node