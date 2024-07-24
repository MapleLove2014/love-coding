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
    def sumNumbers2(self, root) -> int:
        def s(root, n):
            if not root:
                return []
            if not root.left and not root.right:
                return [n + str(root.val)]
            r = []
            if root.left:
                r += s(root.left, n + str(root.val))
            if root.right:
                r += s(root.right, n + str(root.val))
            return r
        return sum([int(n) for n in s(root, "")])

