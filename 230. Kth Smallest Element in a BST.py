# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) == 0:
                return None

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
