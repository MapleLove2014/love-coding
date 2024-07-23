# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def search(root, d):
            if not root:
                return sys.maxsize
            if not root.left and not root.right:
                # leaf
                return 1 + d
        
            return min(search(root.left, 1 + d), search(root.right, 1 + d))
        return search(root, 0)
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1  + min([ self.minDepth2(node) if node else 2**31 for node in [root.left, root.right]])



