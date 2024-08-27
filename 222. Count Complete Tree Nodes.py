# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = [root]
        while len(queue) > 0:
            count += len(queue)
            newQueue = []
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue
        return count

    def ologn(self, root):
        def height(root, dir=True):
            result = 0
            while root:
                result += 1
                root = root.left if dir else root.right
            return result
        if not root:
            return 0
        
        left = height(root.left, True)
        right = height(root.right, False)
        if left == right:
            return 2 ** (left+1) - 1
        return self.ologn(root.left) + self.ologn(root.right) + 1
    
    def countNodes2(self, root) -> int:
        if not root:
            return 0
        c = root
        lh = 0
        while c:
            lh += 1
            c = c.left
        c = root
        rh = 0
        while c:
            rh += 1
            c = c.right
        if lh == rh:
            return 2 ** lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        


