# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        def doFind(root, targetSum, prefix, result):
            if not root:
                return
            if root.val - targetSum == 0 and not root.left and not root.right:
                result.append(prefix + [root.val])
                return
            doFind(root.left, targetSum - root.val, prefix + [root.val], result)
            doFind(root.right, targetSum - root.val, prefix + [root.val], result)
        doFind(root, targetSum, [], result)
        return result