# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        mem = {}
        def doRob(root, amount=0, alert=True):
            if not root:
                return amount
            if root not in mem:
                mem[root] = [0, 0]
            index = 0 if alert else 1
            if mem[root][index] > 0:
                return mem[root][index]
            maxAmount = 0
            if alert:
                maxAmount = max(doRob(root.left, amount, False) + doRob(root.right, amount, False), 
                    doRob(root.left, amount, True) + doRob(root.right, amount, True),
                    doRob(root.left, amount, False) + doRob(root.right, amount, True),
                    doRob(root.left, amount, True) + doRob(root.right, amount, False),
                    )
            else:
                maxAmount = max(doRob(root.left, amount, True) + doRob(root.right, amount, True) + root.val, 
                    doRob(root.left, amount, False) + doRob(root.right, amount, False)
                    )
            mem[root][index] = maxAmount
            return maxAmount
        return doRob(root, 0, False)

    def rob2(self, root):
        def doRob(root):
            left, leftChildren = doRob(root.left) if root.left else (0,0)
            right, rightChildren = doRob(root.right) if root.right else (0,0)
            return leftChildren + rightChildren + root.val, max(left, leftChildren) + max(right, rightChildren)
        return max(doRob(root))