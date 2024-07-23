# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            result.append([node.val for node in queue])
            newQueue = []
            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue

        return result
                
    def levelOrder2(self, root):
        stack = [root]
        result = []
        while stack:
            news = []
            l = []
            for e in stack:
                if e:
                    l.append(e.val)
                    news.append(e.left)
                    news.append(e.right)
            if l:
                result.append(l)
            stack=news
        return result