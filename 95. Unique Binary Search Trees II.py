# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def p(self, level=0):
        x="\t"*level + str(self.val) + "\n"
        if self.left:
            x += "L:" + self.left.p(level+1)
        if self.right:
            x += "R:" + self.right.p(level+1)
        return x

class Solution:
    def generateTrees(self, n: int):
        def g(i, j):
            if i > j:
                return [None]
            if i == j:
                return [TreeNode(i)]
            result = []
            for k in range(i, j+1):
                lefts  = g(i, k-1)
                rights = g(k+1, j)
                for l in lefts:
                    for r in rights:
                        result.append(TreeNode(k, l, r))
            return result
        return g(1, n)

s = Solution()
for t in s.generateTrees(4):
    print(t.p())


                


        