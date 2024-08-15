
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            result.append(queue[-1].val)
            newQueue = []
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue
        return result

    def rightSideView2(self, root):
        stack = [root]
        t = []
        while stack:
            n = []
            t.append(None)
            for node in stack:
                if node:
                    t[-1] = node.val
                    n.append(node.left)
                    n.append(node.right)
            stack = n
        return t if t[-1] != None else t[:-1]