
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
            if left and parent.right:
                root.next = parent.right
            if root.right and root.next:
                root.right.next = root.next.left if root.next.left else root.next.right
            elif root.left and root.next:
                root.left.next = root.next.left if root.next.left else root.next.right
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

    def hori(self, root):

        if not root:
            return root
        

        stack = [root]

        while len(stack) > 0:
            preNode = None
            node = None
            for node in reversed(stack):
                node.next = preNode
                preNode = node

            newStack = []
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            stack = newStack
        return root
            




