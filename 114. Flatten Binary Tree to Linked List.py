# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(root):
            if not root:
                return None
            flattenedLeft = flat(root.left)
            flattenedRight = flat(root.right)
            if flattenedLeft:
                node = flattenedLeft
                while node.right:
                    node = node.right
                node.right = flattenedRight
            else:
                flattenedLeft = flattenedRight
            root.left = None
            root.right = flattenedLeft
            return root
        flat(root)
    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        r = []
        while True:
            while root:
                r.append(root)
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop().right
        h = TreeNode()
        x = h
        for t in r:
            t.left = None
            t.right = None
            x.right = t
            x = t
        return h.right