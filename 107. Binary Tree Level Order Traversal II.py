# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        node = None
        while len(queue) > 0:
            result.append([node.val for node in queue])
            newQueue = []
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue
        return reversed(result)
    
    def levelOrderBottom2(self, root):
        queue=[root]
        result = []
        while queue:
            nq = []
            l=[]
            for q in queue:
                if q:
                    l.append(q.val)
                    nq.append(q.left)
                    nq.append(q.right)
            if l:
                result.append(l)
            queue = nq
        return result[::-1]


