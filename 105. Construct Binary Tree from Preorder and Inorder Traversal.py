# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        def doBuild(preorder, inorder):
            if not preorder or len(preorder) == 0:
                return None
            root = TreeNode(preorder[0])

            rootIndex = inorder.index(root.val)
            root.left = doBuild(preorder[1:rootIndex + 1], inorder[0:rootIndex])
            if len(preorder) >  rootIndex + 1:
                root.right = doBuild(preorder[rootIndex + 1 : ], inorder[rootIndex + 1 : ])
            return root
        return doBuild(preorder, inorder)
        
