# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        def doBuild(inorder, postorder):
            if len(inorder) == 0:
                return None
        
            root = TreeNode(postorder[-1])

            rootIndex = inorder.index(root.val)

            root.left = doBuild(inorder[0:rootIndex], postorder[0:rootIndex])
            root.right = doBuild(inorder[rootIndex+1 : ], postorder[rootIndex:-1])
            return root
        return doBuild(inorder, postorder)
    def buildTree2(self, inorder, postorder):
        def build(inorder, postorder):
            if not postorder:
                return None
            root=TreeNode(postorder[-1])
            rootI=inorder.index(root.val)
            root.left = build(inorder[0:rootI], postorder[0:rootI])
            root.right= build(inorder[rootI+1:], postorder[rootI:-1])
            return root
        return build(inorder, postorder)

        
