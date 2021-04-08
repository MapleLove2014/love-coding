
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        old2new = {}
        dummy = Node(0)
        newTail = dummy
        node = head
        while node:
            newNode = Node(node.val, None, node.random)
            newTail.next = newNode
            old2new[node] = newNode
            node = node.next
            newTail = newNode
        node = dummy.next
        while node:
            if node.random:
                node.random = old2new[node.random]
            node = node.next
        return dummy.next

        
s = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n1.random = n3
n2.random = n1
n3.random = n1

s.copyRandomList(n1)
