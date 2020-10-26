# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        if n <= 0:
            return []
        return self.search((1, n))

    def search(self, nrange):
        n, x = nrange
        if n > x:
            return [None]
        if n == x:
            return [TreeNode(n)]
        result = []
        for i in range(n, x+1):
            root = TreeNode(i)
            lefts = self.search((n, i-1))
            rights = self.search((i+1, x))
            if not lefts or not rights:
                continue
            for left in lefts:
                for right in rights:
                    root.left = left
                    root.right = right
                    result.append(self.copyTree(root))
        return result
            
    def copyTree(self, root):
        if not root:
            return root
        cp = TreeNode(root.val)
        cp.left = self.copyTree(root.left)
        cp.right = self.copyTree(root.right)
        return cp

s = Solution()
print(len(s.generateTrees(5)) == 42)



