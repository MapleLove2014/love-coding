# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def road(root, node):
            t = []
            while root:
                t.append(root)
                if root.val == node.val:
                    return t
                elif root.val > node.val:
                    root = root.left
                else:
                    root = root.right
        t1 = road(root, p)
        t2 = road(root, q)
        l = root
        for i in range(min(len(t1), len(t2))):
            if t1[i] != t2[i]:
                return l
            l = t1[i]
        return l
    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root




