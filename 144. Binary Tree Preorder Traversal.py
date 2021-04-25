# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []

        result = []
        stack = []
        node = root
        while True:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            if len(stack) == 0:
                return result
            node = stack.pop()
            node = node.right
            
    def recurse(self, root):
        if not root:
            return []

        def preorder(root, result):
            if not root:
                return
            result.append(root.val)
            preorder(root.left, result)
            preorder(root.right, result)
        result = []
        preorder(root, result)
        return result
        

