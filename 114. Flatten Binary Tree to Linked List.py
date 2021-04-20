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