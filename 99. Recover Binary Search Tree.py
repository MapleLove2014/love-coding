# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        prev = None
        f1=None
        f2=None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            l = stack.pop()
            if not f1 and prev and prev.val >= l.val:
                f1 = prev
            if prev and prev.val >= l.val and f1:
                f2 = l
            prev = l
            root = l.right
        f1.val, f2.val = f2.val, f1.val




s = Solution()
r = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
s.recoverTree(r)
print("123")

#    1
# 3     4
#   2
# inorder traverse must be two unorderd number 3 2 1 4
# For example array: 1 2 3 4 5 6 7
# -> swap random two elments -> 1 2 6 4 5 3 7 (swap 3 and 6)
# first: prev=6 > l=4, prev is the fist mistake
# then: second mistake set to 4 and keep on looking for another one node so that p > l, then l is the second mistake