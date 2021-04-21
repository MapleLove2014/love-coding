
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def connectLeft(root, parent, left):
            if not root:
                return
            if left:
                root.next = parent.right
            if root.right:
                root.right.next = root.next.left
            connectLeft(root.left, root, True)
            connectLeft(root.right, root, False)


        def connectRight(root, parent):
            if not root:
                return
            connectLeft(root.left, root, True)
            connectRight(root.right, root)
        connectLeft(root.left, root, True)
        connectRight(root.right, root)
        return root