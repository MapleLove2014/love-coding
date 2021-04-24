# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        def doit(root, prefix):
            if not root.left and not root.right:
                return int(prefix + str(root.val))
            result = 0
            if root.left:
                result += doit(root.left, prefix + str(root.val))
            if root.right:
                result += doit(root.right, prefix + str(root.val))
            return result
        
        return doit(root, '')

