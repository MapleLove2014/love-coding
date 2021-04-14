# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def traversal(root, result):
            if not root:
                return
            traversal(root.left, result)
            result.append(root.val)
            traversal(root.right, result)

        result = []
        traversal(root, result)
        return result

    def stack(self, root):
        if not root:
            return []
        
        stack = []
        result = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) == 0:
                return result
            node = stack.pop()
            result.append(node.val)
            node = node.right