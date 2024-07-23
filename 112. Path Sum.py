# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        left = False
        right = False
        if root.left:
            left = self.hasPathSum(root.left, targetSum - root.val)
        if left:
            return True
        if root.right:
            return self.hasPathSum(root.right, targetSum - root.val)
        return False
    def hasPathSum2(self, root, targetSum: int) -> bool:
        if not root:
            return False
        if targetSum == root.val and not root.left and not root.right:
            return True
        return self.hasPathSum2(root.left, targetSum - root.val) or self.hasPathSum2(root.right, targetSum - root.val)
            