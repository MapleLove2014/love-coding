# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def path(root, node, result):
            result.append(root)
            if root.val == node.val:
                return True
            if root.left and path(root.left, node, result):
                return True
            if root.right and path(root.right, node, result):
                return True
            result.pop()
            return False
        ppath = []
        path(root, p, ppath)
        qpath = []
        path(root, q, qpath)
        pre = None
        for i in range(min(len(ppath), len(qpath))):
            if ppath[i].val != qpath[i].val:
                return pre
            pre = ppath[i]
        return pre

s = Solution()

root = TreeNode(1, TreeNode(2), TreeNode(3))

result = s.lowestCommonAncestor(root, root.left, root.right)
print(result.val)


