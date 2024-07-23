# Definition for a binary tree node.
from operator import truediv


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def inner(p, q):
            if not p and not q:
                return True
            if p and q:
                if p.val == q.val:
                    return inner(p.left, q.right) and inner(p.right, q.left)
            return False
        return inner(root.left, root.right)
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def check(m, n):
            if not m and not n:
                return True
            return False if not m or not n or m.val != n.val else check(m.left, n.right) and check(m.right, n.left)
        return check(root.left, root.right)
        