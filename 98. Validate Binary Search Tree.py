# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = None

        node = root
        while True:

            while node:
                stack.append(node)
                node = node.left

            if len(stack) == 0:
                return True
            node = stack.pop()
            if prev != None and node.val <= prev:
                return False
            prev = node.val
            node = node.right

    def twoEndian(self, root):


        def valid(node, bottom, top):
            if not node:
                return True
            if node.val <= bottom or node.val >= top:
                return False
            return valid(node.left, bottom, node.val) and valid(node.right, node.val, top)
        
        return valid(root, float('-inf'), float('inf'))





