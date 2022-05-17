# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        

        def s(node, isLeft=True):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            return s(node.left) + s(node.right, False)
        return s(root, False)