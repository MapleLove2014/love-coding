# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def post(root, result):
            if not root:
                return
            post(root.left, result)
            post(root.right, result)
            result.append(root.val)
        result = []
        post(root, result)
        return result
    def postorderTraversal2(self, root):
        def p(root):
            if not root:
                return []
            return p(root.left) + p(root.right) + [root.val]
        return p(root)


