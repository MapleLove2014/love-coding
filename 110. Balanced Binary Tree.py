# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        if not root:
            return True
        diff = height(root.left) - height(root.right)
        return abs(diff) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def isBalanced2(self, root) -> bool:
        def check(root):
            if not root:
                return True, 0
            l,lh = check(root.left)
            r,rh = check(root.right)
            if not l or not r or abs(lh-rh) > 1:
                return False, 0
            return True, 1 + max(lh, rh)
        return check(root)[0]
