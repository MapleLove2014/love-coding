# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def numTrees(self, n):
        if n <= 0:
            return 0
        mem = [[0] * (n+2) for _ in range(n+2)]
        return self.search((1, n), mem)

    def search(self, nrange, mem):
        n, x = nrange
        if n >= x:
            return 1
        if mem[n][x] != 0:
            return mem[n][x]
        count = 0
        for i in range(n, x+1):
            root = TreeNode(i)
            lefts = self.search((n, i-1), mem)
            rights = self.search((i+1, x), mem)
            if lefts <= 0 or rights <= 0:
                continue
            count += lefts * rights
        mem[n][x] = count
        return count

s = Solution()
print(s.numTrees(5) == 42)
print(s.numTrees(15))



