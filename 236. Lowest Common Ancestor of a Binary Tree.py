# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def road(root, node, prefix):
            if not root:
                return []
            if root == node:
                return prefix + [root]
            l = road(root.left, node, prefix + [root])
            if l:
                return l
            r = road(root.right, node, prefix + [root])
            if r:
                return r
        t1 = road(root, p, [])
        t2 = road(root, q, [])
        l = root
        for i in range(min(len(t1), len(t2))):
            if t1[i] != t2[i]:
                return l
            l = t1[i]
        return l
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p:
            return p
        if root == q:
            return q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l and r:
            return r
        if l and not r:
            return l
        if l and r:
            return root
        return None

s = Solution()

root = TreeNode(1, TreeNode(2), TreeNode(3))

result = s.lowestCommonAncestor(root, root.left, root.right)
print(result.val)


