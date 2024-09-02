# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ls = self.binaryTreePaths(root.left)
        rs = self.binaryTreePaths(root.right)
        return [ str(root.val) + "->" + p for p in ls + rs] if (ls + rs) else [str(root.val)]
    

s = Solution()
print(s.binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
print(s.binaryTreePaths(TreeNode(1, TreeNode(2), TreeNode(3))))